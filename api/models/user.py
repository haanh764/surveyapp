from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database.db_config import Base, session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    isActivated = Column(Boolean, nullable=False, default=False)
    isBlocked = Column(Boolean, nullable=False, default=False)
    surveys = relationship("Survey", back_populates="users", cascade="all, delete-orphan")

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.isActivated = False
        self.isBlocked = False

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'isActivated': self.isActivated,
            'isBlocked': self.isBlocked
        }
    
    def generate_password(self):
        self.password = generate_password_hash(self.password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def find_by_email(email):
        return session.query(User).filter_by(email=email).first()

    def find_by_id(id):
        return session.query(User).filter_by(id=id).first()

    def add_user(self):
        session.add(self)
        session.commit()

    def delete_user(self):
        session.delete(self)
        session.commit()

    def get_all_users():
        return session.query(User).all()
