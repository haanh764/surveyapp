# Example for create resource for API
from flask_restful import Resource
from sqlalchemy.sql import text
from database.db_connector import DbConnector
from flask_jwt_extended  import jwt_required
from common.authentication_helper import admin_required
from models.user import User
from database.db_connector import db_connector
import io


class DbTesting(Resource):
    def __init__(self):
        pass

    def get(self):                
        return {'message': db_connector.get_model_by_id(User, 1).__str__()}
