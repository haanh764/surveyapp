from sqlalchemy import Column, Integer, String, ForeignKey
from database.db_config import Base, session
from sqlalchemy.orm import relationship
from models.survey import Survey, Responses, Respondents


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

    def delete_respondent(self):
        session.delete(self)
        session.commit()

    @staticmethod
    def get_respondents(surveyId):
        return session.query(AllowedRespondents).filter_by(surveyId=surveyId)
