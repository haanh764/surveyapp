import datetime
from common.authentication_helper import generate_confirmation_token, confirm_token
from common.settings import MAIL_USERNAME
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies
from models.admin import Admin
from models.revoked_token import RevokedToken
from common.authentication_helper import admin_required
from app import jwt, app

@app.after_request
def refresh_expiring_access_tokens(response):
    try:
        expire_timestamp = get_jwt()["exp"]
        now = datetime.datetime.utcnow()
        target_timestamp = datetime.datetime.timestamp(now + datetime.timedelta(minutes=30))
        if target_timestamp > expire_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
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
