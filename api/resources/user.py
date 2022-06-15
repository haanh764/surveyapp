from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

class ChangePassword(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        current_user = User.find_by_id(current_user_id)
        current_user.password = data['new_password']
        current_user.generate_password()
        current_user.add_user()
        return {'message': 'Password was changed'}, 200

class DeleteUser(Resource):
    @jwt_required()
    def delete(self):
        current_user_id = get_jwt_identity()
        current_user = User.find_by_id(current_user_id)
        current_user.delete_user()
        return {'message': 'Your account has been successfully deleted'}, 200

class isBlocked(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        current_user = User.find_by_id(current_user_id)
        if current_user.isBlocked:
            return {'message': 'User {} is blocked'.format(current_user.email)}, 201
        else:
            return {'message': 'User {} is not blocked'.format(current_user.email)}, 200
            