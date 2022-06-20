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
    isSurveySentAutomatically = Column(Boolean, nullable=True)
    startDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    endDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    creationDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    modificationDate = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    users = relationship("User", back_populates="surveys")
    questions = relationship("Question", back_populates="survey", cascade="all, delete-orphan")
    respondents = relationship("AllowedRespondents", back_populates="survey", cascade="all, delete-orphan")
    responses = relationship("Responses", back_populates="survey", cascade="all, delete-orphan")

    def __init__(self, surveyOwner, title, description, startDate, endDate, isPublic=False, isSurveySentAutomatically=False):
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
        self.isSurveySentAutomatically = isSurveySentAutomatically
        self.generate_hash()

    def modify(self, title, description, startDate, endDate, isPublic=False, isSurveySentAutomatically=None):
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
        if isSurveySentAutomatically is not None:
            self.isSurveySentAutomatically = isSurveySentAutomatically
        for allowed_respondent in self.respondents:
            allowed_respondent.delete_respondent()
        for response in self.responses:
            response.delete_response()

    def generate_hash(self):
        str = string.ascii_lowercase + string.ascii_uppercase
        self.surveyHash = ''.join(random.choice(str) for _ in range(30))

    def check_hash(self, surveyHash):
        return self.surveyHash == surveyHash

    def is_published(self):
        return datetime.datetime.now(datetime.timezone.utc).timestamp() >= self.startDate.timestamp() and datetime.datetime.now(datetime.timezone.utc).timestamp() <= self.endDate.timestamp()

    def serialize(self):
        return {
            'id': self.id,
            'surveyOwner': self.surveyOwner,
            'title': self.title,
            'description': self.description,
            'isPublic': self.isPublic,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'isPublished': self.is_published(),
            'isSurveySentAutomatically': self.isSurveySentAutomatically,
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
        survey_json['config']['isSurveySentAutomatically'] = survey_dict['isSurveySentAutomatically']
        emails = list()
        for allowed_respondent in self.respondents:
            emails.append(allowed_respondent.respondent.email)
        emails = list(set(emails))
        survey_json['config']['emails'] = emails
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
                options['step'] = scale_question.step
                options['defaultValue'] = scale_question.defaultValue
                options['min'] = scale_question.min_value
                options['max'] = scale_question.max_value
                pass
            elif open_answer_question:
                open_answer_question = open_answer_question[0]
                options['defaultValue'] = open_answer_question.defaultValue
                options['placeholder'] = open_answer_question.placeholder
                question_data['type'] = 'input'
                pass
            elif multiple_choice_question:
                multiple_choice_question = multiple_choice_question[0]
                if multiple_choice_question.allowMultipleAnswers:
                    question_data['type'] = 'checkbox'
                    models[question.model] = list()
                else:
                    question_data['type'] = 'radio'
                options = dict()
                options_in_options = list()
                default_values = list()
                for i, answer_option in enumerate(multiple_choice_question.answer_options):
                    options_in_options.append(answer_option.serialize())
                    if answer_option.defaultValue:
                        default_values.append(i)
                options['options'] = options_in_options
                if multiple_choice_question.allowMultipleAnswers:
                    options['defaultValue'] = default_values
                else:
                    if default_values:
                        options['defaultValue'] = default_values[0]
                    else:
                        options['defaultValue'] = ''
            else:
                options['defaultValue'] = question.defaultValue
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

    def get_all_surveys():
        return session.query(Survey).all()


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

    def delete_respondent(self):
        session.delete(self)
        session.commit()

    @staticmethod
    def get_respondent(email):
        return session.query(Respondents).filter_by(email=email).first()


class Responses(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True, index=True)
    respondentId = Column(Integer, ForeignKey(Respondents.id), nullable=True)
    surveyId = Column(Integer, ForeignKey(Survey.id), nullable=False)
    survey = relationship("Survey", back_populates="responses")
    respondent = relationship("Respondents", back_populates="responses")
    answers = relationship("Answers", back_populates="response", cascade="all, delete-orphan")

    def __init__(self, respondentId, surveyId):
        self.respondentId = respondentId
        self.surveyId = surveyId

    def add_response(self):
        session.add(self)
        session.commit()

    def delete_response(self):
        session.delete(self)
        session.commit()

    @staticmethod
    def get_responses(surveyId):
        return session.query(AllowedRespondents).filter_by(surveyId=surveyId)


from models.question import Question, ScaleQuestion, OpenAnswerQuestion, MultipleChoiceQuestion, AnswerOption


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    responseId = Column(Integer, ForeignKey(Responses.id), nullable=False)
    response = relationship("Responses", back_populates="answers")
    open_answers = relationship("OpenAnswers", back_populates="answer", cascade="all, delete-orphan")
    scale_answers = relationship("ScaleAnswers", back_populates="answer", cascade="all, delete-orphan")
    choice_answers = relationship("ChoiceAnswers", back_populates="answer", cascade="all, delete-orphan")

    def __init__(self, responseId):
        self.responseId = responseId

    def add_answer(self):
        session.add(self)
        session.commit()


class OpenAnswers(Base):
    __tablename__ = 'open_answers'
    id = Column(Integer, primary_key=True, index=True)
    answerId = Column(Integer, ForeignKey(Answers.id), nullable=False)
    answer = relationship("Answers", back_populates="open_answers")
    open_answer_question_id = Column(Integer, ForeignKey(OpenAnswerQuestion.id), nullable=False)
    open_question = relationship("OpenAnswerQuestion", back_populates="open_answers")
    answer_text = Column(String(255), nullable=False)

    def __init__(self, answerId, open_answer_question_id, answer_text):
        self.answerId = answerId
        self.open_answer_question_id = open_answer_question_id
        self.answer_text = answer_text

    def add_answer(self):
        session.add(self)
        session.commit()


class ScaleAnswers(Base):
    __tablename__ = 'scale_answers'
    id = Column(Integer, primary_key=True, index=True)
    answerId = Column(Integer, ForeignKey(Answers.id), nullable=False)
    answer = relationship("Answers", back_populates="scale_answers")
    scale_question_id = Column(Integer, ForeignKey(ScaleQuestion.id), nullable=False)
    scale_question = relationship("ScaleQuestion", back_populates="scale_answers")
    value = Column(Integer, nullable=False)

    def __init__(self, answerId, scale_question_id, value):
        self.answerId = answerId
        self.scale_question_id = scale_question_id
        self.value = value

    def add_answer(self):
        session.add(self)
        session.commit()


class ChoiceAnswers(Base):
    __tablename__ = 'choice_answers'
    id = Column(Integer, primary_key=True, index=True)
    answerId = Column(Integer, ForeignKey(Answers.id), nullable=False)
    answer = relationship("Answers", back_populates="choice_answers")
    multiple_choice_questionsId = Column(Integer, ForeignKey(MultipleChoiceQuestion.id), nullable=False)
    choice_question = relationship("MultipleChoiceQuestion", back_populates="choice_answers")
    answer_options_choice = relationship("AnswerOptionsChoiceAnswer", back_populates="choiceAnswer", cascade="all, delete-orphan")

    def __init__(self, answerId, multiple_choice_questionsId):
        self.answerId = answerId
        self.multiple_choice_questionsId = multiple_choice_questionsId

    def add_answer(self):
        session.add(self)
        session.commit()


class AnswerOptionsChoiceAnswer(Base):
    __tablename__ = 'answer_options_choice_answer'
    id = Column(Integer, primary_key=True, index=True)
    choice_answerId = Column(Integer, ForeignKey(ChoiceAnswers.id), nullable=False)
    choiceAnswer = relationship("ChoiceAnswers", back_populates="answer_options_choice")
    answer_optionId = Column(Integer, ForeignKey(AnswerOption.id), nullable=False)
    answer_option = relationship("AnswerOption", back_populates="answer_options_choice_answers")

    def __init__(self, choice_answerId, answer_optionId):
        self.choice_answerId = choice_answerId
        self.answer_optionId = answer_optionId

    def add_answer(self):
        session.add(self)
        session.commit()

