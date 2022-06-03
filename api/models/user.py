from xmlrpc.client import Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean
from database.db_config import Base, session

class User(Base):
    __tablename__ = 'user_test'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    isConfirmed = Column(Boolean, nullable=False, default=False)
    isBlocked = Column(Boolean, nullable=False, default=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.isConfirmed = False
        self.isBlocked = False

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'isConfirmed': self.isConfirmed,
            'isBlocked': self.isBlocked
        }
    
    def generate_password(self):
        self.password = generate_password_hash(self.password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def find_by_email(email):
        return session.query(User).filter_by(email=email).first()

    def add_user(self):
        session.add(self)
        session.commit()
