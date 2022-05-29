# Example for create resource for API
from flask_restful import Resource
from common.db_connector import DbConnector

class Home(Resource):
  def __init__(self):
    self.db_connector = DbConnector()

  def get(self):
    query = "SHOW TABLES"
    res = self.db_connector.connection.execute(query)
    rows = res.fetchall()
    return {'message': rows[0][0]}
