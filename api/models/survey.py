import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database.db_config import Base, session
from sqlalchemy.orm import relationship
from .user import User


class Survey(Base):
    __tablename__ = 'surveys'
    id = Column(Integer, primary_key=True, index=True)
    surveyOwner = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    startDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    endDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    creationDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    modificationDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    users = relationship("User", back_populates="surveys")
    questions = relationship("Question", back_populates="survey", cascade="all, delete-orphan")

    def __init__(self, surveyOwner, title, description, startDate, endDate):
        self.surveyOwner = surveyOwner
        self.title = title
        self.description = description
        if not startDate:
            self.startDate = datetime.datetime.now(datetime.timezone.utc)
        else:
            self.startDate = startDate
        if not endDate:
            self.endDate = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        else:
            self.endDate = endDate

    def serialize(self):
        return {
            'id': self.id,
            'surveyOwner': self.surveyOwner,
            'title': self.title,
            'description': self.description,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'creationDate': self.creationDate,
            'modificationDate': self.modificationDate
        }

    def add_survey(self):
        session.add(self)
        session.commit()
    
    def list_surveys_by_user(user_id):
        return session.query(Survey).filter_by(surveyOwner=user_id).all()
