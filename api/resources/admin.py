import datetime
from common.authentication_helper import generate_confirmation_token, confirm_token
from common.settings import MAIL_USERNAME
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from models.admin import Admin, RevokedToken
from common.authentication_helper import admin_required

class AdminLogin(Resource):
    def post(self):
        data = request.get_json()
        admin = Admin.find_by_email(data['email'])
        if admin and admin.check_password(data['password']):
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=admin.id, expires_delta=expires)
            return {'access_token': access_token}, 200

class AdminLogout(Resource):
    @jwt_required()
    @admin_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}, 200
        except:
            return {'message': 'Something went wrong'}, 500
