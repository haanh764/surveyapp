from sqlalchemy import Column, Integer, String, event
from database.db_config import Base
from database.db_connector import db_connector
from werkzeug.security import check_password_hash, generate_password_hash
from common.settings import ADMIN_PSWD, MAIL_USERNAME


class Admin(Base):
    __tablename__ = 'administrators'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Admin %r>' % self.email

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
        }

    def generate_password(self):
        self.password = generate_password_hash(self.password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def init_admin_default():
        Base.metadata.create_all(bind=db_connector.engine)
        if not db_connector.find_model_by_email(Admin, MAIL_USERNAME):
            admin = Admin(MAIL_USERNAME, ADMIN_PSWD)
            admin.generate_password()
            db_connector.add_model_to_db(admin)
