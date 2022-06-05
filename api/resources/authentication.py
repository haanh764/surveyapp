from flask import request, Response
from flask_restful import Resource, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.user import User
import datetime
from email_validator import validate_email, EmailNotValidError
from common.authentication_helper import generate_confirmation_token, confirm_token, send_email

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        try:
            validate_email(data['email'])
            existing_user = User.find_by_email(data['email'])
            if existing_user:
                return {'message': 'User {} already exists. Please Login or Signup with another email!'.format(data['email'])}
            user = User(**data)
            user.generate_password()
            user.add_user()
            token = generate_confirmation_token(data['email'])
            confirm_url = url_for('activateaccount', token=token, _external=True)
            send_email(data['email'], 'Please Confirm Your Email', confirm_url)
            return {'message': 'User {} was created. Please check your email for activation link!'.format(user.email)}, 200
        except EmailNotValidError as errorMsg:
            return {'message': 'Invalid email address. {}'.format(errorMsg)}, 400

class ActivateAccount(Resource):
    def get(self, token):
        email = confirm_token(token)
        if email:
            user = User.find_by_email(email)
            if user.isActivated:
                return {'message': 'User {} is already confirmed.'.format(email)}, 200
            user.isActivated = True
            user.add_user()
            return {'message': 'User {} was confirmed'.format(user.email)}, 200
        else:
            return {'message': 'The confirmation link is invalid or has expired.'}, 400

class NotActivated(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        current_user = User.find_by_id(current_user_id)
        if current_user.isActivated == False:
            return {'message': 'User {} is not activated'.format(current_user.email)}, 200

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user and user.check_password(data['password']):
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=user.id, expires_delta=expires)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid username or password'}, 401

class Logout(Resource):
    @jwt_required()
    def post(self):
        return {'message': 'User logged out'}, 200
