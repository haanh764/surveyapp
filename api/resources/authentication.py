from flask import Response, request
from flask_restful import Resource
from models.user import User
from flask_login import login_user, logout_user, login_required

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            login_user(user)
            return Response('Logged in successfully.', status=200)
        else:
            return Response('Wrong email or password.', status=401)

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user:
            return Response('User already exists.', status=401)
        else:
            user = User(data['email'], data['password'])
            user.generate_password()
            user.save()
            login_user(user)
            return Response('Signed up successfully.', status=200)

class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return Response('Logged out successfully.', status=200)
