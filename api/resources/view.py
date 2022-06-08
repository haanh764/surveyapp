# Example for create resource for API
from flask_restful import Resource
from database.db_connector import DbConnector
from flask_jwt_extended  import jwt_required
from common.authentication_helper import admin_required

class Home(Resource):
  def __init__(self):
    self.db_connector = DbConnector()

  @jwt_required()
  @admin_required()
  def get(self):
    query = "SHOW TABLES"
    res = self.db_connector.connection.execute(query)
    rows = res.fetchall()
    return {'message': rows[0][0]}
