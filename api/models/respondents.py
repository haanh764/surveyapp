from sqlalchemy import Column, Integer, String, ForeignKey
from database.db_config import Base, session
from sqlalchemy.orm import relationship
from models.survey import Survey


class Respondents(Base):
    __tablename__ = 'respondents'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)
    surveys = relationship("AllowedRespondents", back_populates="respondent", cascade="all, delete-orphan")
    responses = relationship("Responses", back_populates="respondent", cascade="all, delete-orphan")

    def __init__(self, email):
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email
        }

    def add_respondent(self):
        if not session.query(Respondents).filter_by(email=self.email).first():
            session.add(self)
            session.commit()

    @staticmethod
    def get_respondent(email):
        return session.query(Respondents).filter_by(email=email).first()


class AllowedRespondents(Base):
    __tablename__ = 'allowed_respondents'
    id = Column(Integer, primary_key=True, index=True)
    respondentId = Column(Integer, ForeignKey(Respondents.id), nullable=False)
    surveyId = Column(Integer, ForeignKey(Survey.id), nullable=False)
    survey = relationship("Survey", back_populates="respondents")
    respondent = relationship("Respondents", back_populates="surveys")

    def __init__(self, respondentId, surveyId):
        self.respondentId = respondentId
        self.surveyId = surveyId

    def add_allowed_respondent(self):
        session.add(self)
        session.commit()

    @staticmethod
    def get_respondents(surveyId):
        return session.query(AllowedRespondents).filter_by(surveyId=surveyId)
