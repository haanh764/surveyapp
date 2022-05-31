from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models.user import User
import datetime

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        user = User(**data)
        user.generate_password()
        user.add_user()
        id = user.id
        return {'message': 'User {} was created'.format(id)}, 200

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
