from sqlalchemy import create_engine
from common.settings import DB_URL

from datetime import date, datetime
from decimal import Decimal

class DbConnector():
    def __init__(self):
        self.engine = create_engine(DB_URL)
        self.connection = self.engine.connect()
    
    def get_connection(self):
        return self.connection
    
    def close_connection(self):
        self.connection.close()
    
    def clean_select_row(self, row, keys):
        try:
            clean_row = [str(field) if isinstance(field, datetime) or isinstance(
                field, Decimal) or isinstance(field, date) else field for field in list(row)]
            current_row = {}
            for i in range(len(keys)):
                current_row[keys[i]] = clean_row[i]
            return current_row
        except:
            return None

    def clean_select_results(self, data, keys):
        if len(data) == 0:
            return {}
        result_data = []
        for row in data:
            result_data.append(self.clean_select_row(row, keys))
        return result_data
