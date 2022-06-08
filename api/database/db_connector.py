from typing import Literal
from sqlalchemy import create_engine, select, insert, MetaData
from sqlalchemy.engine.cursor import CursorResult
from common.settings import DB_URL

from datetime import date, datetime
from decimal import Decimal

class DbConnector():
    def __init__(self):
        self.engine = create_engine(DB_URL)
        self.connection = self.engine.connect()
        self.meta_data = MetaData(bind=self.connection, reflect=True)

    def get_connection(self):
        return self.connection
        
    def __open_connection__(self):
        self.connection = self.engine.connect()

    def __run_query__(self, query) -> CursorResult:
        self.__open_connection__()
        result = self.connection.execute(query)
        self.__close_connection__()
        return result

    def __close_connection__(self):
        self.connection.close()

    def add_user(self, user_email: Literal, user_password: Literal):
        users_table = self.meta_data.tables['users']
        query = insert(users_table).values(email=user_email, password=user_password)
        self.__run_query__(query)

    def get_user(self, user_email: Literal) -> CursorResult:
        users_table = self.meta_data.tables['users']
        query = select(users_table).where(users_table)
        return self.__run_query__(query)
    
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
