import datetime
import random
import string

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database.db_config import Base, session
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


from .user import User


class Survey(Base):
    __tablename__ = 'surveys'
    id = Column(Integer, primary_key=True, index=True)
    surveyOwner = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    isPublic = Column(Boolean, nullable=True)
    surveyHash = Column(String(30), nullable=True)
    startDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    endDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    creationDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    modificationDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    users = relationship("User", back_populates="surveys")
    questions = relationship("Question", back_populates="survey", cascade="all, delete-orphan")

    def __init__(self, surveyOwner, title, description, startDate, endDate, isPublic=False):
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
        if isPublic:
            self.isPublic = isPublic
        else:
            self.isPublic = False
            self.generate_hash()
    
    def modify(self, title, description, startDate, endDate, isPublic=False):
        self.title = title
        self.description = description
        if startDate:
            self.startDate = startDate
        if endDate:
            self.endDate = endDate
        self.modificationDate = datetime.datetime.now(datetime.timezone.utc)
        if isPublic:
            self.isPublic = isPublic
        else:
            self.isPublic = False
    
    def generate_hash(self):
        str = string.ascii_lowercase + string.ascii_uppercase
        self.surveyHash = ''.join(random.choice(str) for _ in range(30))

    def check_hash(self, surveyHash):
        return self.surveyHash == surveyHash

    def serialize(self):
        return {
            'id': self.id,
            'surveyOwner': self.surveyOwner,
            'title': self.title,
            'description': self.description,
            'isPublic': self.isPublic,
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

    def get_survey(survey_id):
        return session.query(Survey).filter_by(id=survey_id).first()
    
    def get_json(self):
        survey_json = dict()
        survey_dict = self.serialize()
        survey_json['config'] = dict()
        survey_json['data'] = dict()
        survey_json['config']['startDate'] = survey_dict['startDate']
        survey_json['config']['id'] = survey_dict['id']
        survey_json['config']['endDate'] = survey_dict['endDate']
        survey_json['config']['isPublic'] = survey_dict['isPublic']
        survey_json['data']['title'] = survey_dict['title']
        survey_json['data']['description'] = survey_dict['description']
        form_builder = dict()
        models = dict()
        questions = list()
        for question in sorted(self.questions, key=lambda x: x.order_number):
            question_data = question.serialize()
            models[question.model] = None
            scale_question = question.scale_question
            open_answer_question = question.open_answer_question
            multiple_choice_question = question.multiple_choice_question
            options = dict()
            if scale_question:
                scale_question = scale_question[0]
                question_data['type'] = 'slider'
                options['step'] = 1
                options['defaultValue'] = scale_question.min_value
                pass
            elif open_answer_question:
                options['defaultValue'] = None
                options['placeholder'] = None
                question_data['type'] = 'text'
                pass
            elif multiple_choice_question:
                multiple_choice_question = multiple_choice_question[0]
                if multiple_choice_question.allowMultipleAnswers:
                    question_data['type'] = 'checkbox'
                    models[question.model] = list()
                else:
                    question_data['type'] = 'radio'
                options = list()
                for answer_option in multiple_choice_question.answer_options:
                    options.append(answer_option.serialize())
            else:
                options['defaultValue'] = None
                options['tag'] = question.tag
                options['type'] = 'text'
                question_data['type'] = 'text'
            question_data['options'] = options
            questions.append(question_data)
        form_builder['list'] = questions
        form_builder['models'] = models
        survey_json['data']['formBuilder'] = form_builder
        return survey_json

    def find_by_id(id):
        return session.query(Survey).filter_by(id=id).first()

    def delete_survey(self):
        session.delete(self)
        session.commit()
