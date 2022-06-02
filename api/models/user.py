from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String
from database.db_config import Base, session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

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

    def find_by_email(email):
        return session.query(User).filter_by(email=email).first()

    def add_user(self):
        session.add(self)
        session.commit()
