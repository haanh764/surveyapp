from flask_restful import Resource
from database.db_connector import DbConnector

class User(Resource):
  def __init__(self):
    self.db_connector = DbConnector()   