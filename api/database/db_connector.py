from sqlalchemy import create_engine, false, select, insert, MetaData
from sqlalchemy.engine import Connection
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.orm import sessionmaker

from common.settings import DB_URL

from typing import Any
from pip import List
from typing import Literal

from models.user import User

class DbConnector():
    def __init__(self):
        self.engine = create_engine(DB_URL)
        self.connection = Connection(engine=self.engine)
        self.meta_data = MetaData()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

#-------------MODELS-------------------

    def add_model_to_db(self, model) -> None:
        '''
        Args:
            model: object of class derieved from our Base for all models

        Returns: None

        Raises:
            After adding something to database, the database is changed, so if we queried for model from database 
            and now if we want to use 'a' for something we need to reacquire that model from database, as previous reference is no longer valid, 
            you will get DetachedInstanceError if you don't reacquire reference .
                a = get_model_by_id(1)
                a.something = 2
                add_model_to_db(a)
                a.something = 3 -> DetachedInstanceError

                a = get_model_by_id(1)
                a_id = a.id
                a.something = 2
                add_model_to_db(a)
                a = get_model_by_id(a_id)
                a.something = 3 -> It just works!
        '''
        with self.SessionLocal.begin() as session:
            session.expire_on_commit = True
            session.add(model)

    def delete_model_from_db(self, model) -> None:
        '''
        Args:
            model: object of class derieved from our Base for all models

        Returns: None

        Raises:
            After removing something to database, the database is changed, so if we queried for model from database 
            we need to reacquire that model from database, as previous reference is no longer valid, 
            you will get DetachedInstanceError if you don't reacquire reference .
                a = get_model_by_id(1)
                a.something = 2
                delete_model_from_db(a)
                a.something = 3 -> DetachedInstanceError
        '''
        with self.SessionLocal.begin() as session:
            session.expire_on_commit = True
            session.delete(model)

    def get_model_by_id(self, model_class, model_id):
        with self.SessionLocal.begin() as session:
            session.expire_on_commit = False
            return session.get(model_class, model_id)

    def get_all_models(self, model_class) -> List[Any]:
        with self.SessionLocal.begin() as session:
            session.expire_on_commit = False
            return session.query(model_class).all()

    def find_model_by_email(self, model_class, model_email: Literal) -> Any:
        with self.SessionLocal.begin() as session:
            session.expire_on_commit = False
            return session.query(model_class).filter_by(email=model_email).first()

#------------REVOKED_TOKENS------------
    def is_revoked_token_jti_blacklisted(self, cls, jti):
        with self.SessionLocal.begin() as session:
            session.expire_on_commit = False
            query = session.query(cls).filter_by(jti=jti).first()
            return bool(query)


  
db_connector = DbConnector()