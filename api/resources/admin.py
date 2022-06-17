import datetime
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies
from models.admin import Admin
from models.survey import Survey
from models.revoked_token import RevokedToken
from models.user import User
from common.authentication_helper import admin_required, generate_password
from app import jwt, app, mail
from flask_mail import Message

@app.after_request
def refresh_expiring_access_tokens(response):
    try:
        expire_timestamp = get_jwt()["exp"]
        now = datetime.datetime.utcnow()
        target_timestamp = datetime.datetime.timestamp(now + datetime.timedelta(minutes=30))
        if target_timestamp > expire_timestamp:
            access_token = create_access_token(identity=get_jwt_identity(), additional_claims={'is_admin': True})
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response

class AdminLogin(Resource):
    def post(self):
        data = request.get_json()
        admin = Admin.find_by_email(data['email'])
        if admin and admin.check_password(data['password']):
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=admin.id, expires_delta=expires, additional_claims={'is_admin': True})
            response = jsonify({'message': 'Logged in as admin with email {}. Access token is {}'.format(admin.email, access_token)})
            set_access_cookies(response, access_token)
            response.status_code = 200
            return response
        return {'message': 'Invalid username or password'}, 401

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    return RevokedToken.is_jti_blacklisted(jti)

class AdminLogout(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        jti = get_jwt()['jti']
        ttype = get_jwt()['type']
        print(ttype)
        try:
            response = jsonify({'message': 'Admin has logged out'})
            unset_jwt_cookies(response)
            revoked_token = RevokedToken(jti=jti, type=ttype)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}, 200
        except:
            return {'message': 'Something went wrong'}, 500

class ResetUserPassword(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        user_email = request.get_json()['email']
        selected_user = User.find_by_email(user_email)
        if selected_user:
            new_password = generate_password(8)
            selected_user.password = new_password
            selected_user.generate_password()
            selected_user.add_user()
            msg = Message()
            msg.subject = 'Password reset'
            msg.sender = app.config['MAIL_USERNAME']
            msg.recipients = [selected_user.email]
            msg.body = 'Your new password is: {}'.format(new_password)
            mail.send(msg)
            return {'message': 'Password has been reset. New password has been sent to your email!'}, 200
        return {'message': 'User not found'}, 404

class SearchUser(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user:
            return {'message': 'User found', 'user_email': user.email, 'user_activated': user.isActivated, 'user_blocked': user.isBlocked}, 200
        return {'message': 'User not found'}, 404

class ActivateUser(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user and not user.isActivated:
            user.isActivated = True
            user.add_user()
            return {'message': 'User has been activated'}, 200
        return {'message': 'User not found'}, 404

class BlockUser(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user and not user.isBlocked:
            user.isBlocked = True
            user.add_user()
            return {'message': 'User has been blocked'}, 200
        return {'message': 'User not found'}, 404

class UnblockedUser(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user and user.isBlocked:
            user.isBlocked = False
            user.add_user()
            return {'message': 'User has been unblocked'}, 200
        return {'message': 'User not found'}, 404

class AdminDeleteUser(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user:
            user.delete_user()
            return {'message': 'User has been deleted'}, 200
        return {'message': 'User not found'}, 404

class AdminListUsers(Resource):
    @jwt_required()
    @admin_required()
    def get(self):
        users = User.get_all_users()
        users_data = dict()
        for user in users:
            users_data[user.id] = {'user_email': user.email, 'user_activated': user.isActivated, 'user_blocked': user.isBlocked}
        response = jsonify({
            'message': 'Users list has been returned',
            'users': users_data
        })
        response.status_code = 200
        return response

class AdminDeleteSurvey(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        survey = Survey.find_by_id(data['id'])
        if survey:
            survey.delete_survey()
            return {'message': 'Survey has been deleted'}, 200
        return {'message': 'Survey not found'}, 404

class AdminChangePassword(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        data = request.get_json()
        current_admin_id = get_jwt_identity()
        current_admin = Admin.find_by_id(current_admin_id)
        if current_admin:
            current_admin.password = data['new_password']
            current_admin.generate_password()
            current_admin.add_admin()
            return {'message': 'Password has been changed'}, 200
        return {'message': 'Admin not found'}, 404

class AdminListSurveys(Resource):
    @jwt_required()
    @admin_required()
    def get(self):
        surveys = Survey.get_all_surveys()
        surveys_data = dict()
        for survey in surveys:
            surveys_data[survey.id] = survey.serialize()        
        response = jsonify({
            'message': 'Surveys list has been returned',
            'surveys': surveys_data
        })
        response.status_code = 200
        return response
