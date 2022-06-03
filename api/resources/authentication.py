from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models.user import User
import datetime
from email_validator import validate_email, EmailNotValidError

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
            id = user.id
            return {'message': 'User {} was created'.format(id)}, 200
        except EmailNotValidError as errorMsg:
            return {'message': 'Invalid email address. {}'.format(errorMsg)}, 400

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
    @staticmethod
    def post():
        return {'message': 'User logged out'}, 200
