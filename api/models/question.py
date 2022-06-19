import datetime

from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from sqlalchemy.orm import relationship
from database.db_config import Base, session
from .survey import Survey


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    surveyId = Column(Integer, ForeignKey(Survey.id), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    image = Column(MEDIUMBLOB, nullable=True)
    order_number = Column(Integer, nullable=False)
    tag = Column(String(8), nullable=True)
    defaultValue = Column(String(255), nullable=True)
    model_key = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    survey = relationship("Survey", back_populates="questions")
    scale_question = relationship("ScaleQuestion", back_populates="question", cascade="all, delete-orphan")
    open_answer_question = relationship("OpenAnswerQuestion", back_populates="question", cascade="all, delete-orphan")
    multiple_choice_question = relationship("MultipleChoiceQuestion", back_populates="question", cascade="all, delete-orphan")

    def __init__(self, survey_id, title, order_number, defaultValue=None, description=None, tag=None, model_key=None, model=None, image=None):
        self.surveyId = survey_id
        self.title = title
        self.description = description
        self.order_number = order_number
        self.tag = tag
        self.image = image
        self.model_key = model_key
        self.model = model
        self.defaultValue = defaultValue

    def serialize(self):
        return {
            'id': self.id,
            'surveyId': self.surveyId,
            'title': self.title,
            'description': self.description,
            'order': self.order_number,
            'tag': self.tag,
            'image': self.image,
            'key': self.model_key,
            'model': self.model
        }

    def add_question(self):
        session.add(self)
        session.commit()

    def delete_question(self):
        session.delete(self)
        session.commit()

    @staticmethod
    def get_question(model):
        return session.query(Question).filter_by(model=model).first()


class ScaleQuestion(Base):
    __tablename__ = 'scale_questions'
    id = Column(Integer, primary_key=True, index=True)
    questionId = Column(Integer, ForeignKey(Question.id), nullable=False)
    defaultValue = Column(Float, nullable=False)
    step = Column(Float, nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    question = relationship("Question", back_populates="scale_question")
    scale_answers = relationship("ScaleAnswers", back_populates="scale_question", cascade="all, delete-orphan")

    def __init__(self, questionId, min_value, max_value, defaultValue=None, step=None):
        self.questionId = questionId
        self.min_value = min_value
        self.max_value = max_value
        self.defaultValue = defaultValue
        self.step = step

    def serialize(self):
        return {
            'id': self.id,
            'questionId': self.questionId,
            'min': self.min_value,
            'max': self.max_value
        }

    def add_question(self):
        session.add(self)
        session.commit()


class OpenAnswerQuestion(Base):
    __tablename__ = 'open_answer_questions'
    id = Column(Integer, primary_key=True, index=True)
    defaultValue = Column(String(255), nullable=True)
    placeholder = Column(String(255), nullable=True)
    questionId = Column(Integer, ForeignKey(Question.id), nullable=False)
    question = relationship("Question", back_populates="open_answer_question")
    open_answers = relationship("OpenAnswers", back_populates="open_question", cascade="all, delete-orphan")

    def __init__(self, questionId, defaultValue=None, placeholder=None):
        self.questionId = questionId
        self.defaultValue = defaultValue
        self.placeholder = placeholder

    def serialize(self):
        return {
            'id': self.id,
            'questionId': self.questionId
        }

    def add_question(self):
        session.add(self)
        session.commit()


class MultipleChoiceQuestion(Base):
    __tablename__ = 'multiple_choice_questions'
    id = Column(Integer, primary_key=True, index=True)
    questionId = Column(Integer, ForeignKey(Question.id), nullable=False)
    allowMultipleAnswers = Column(Boolean, nullable=False)
    question = relationship("Question", back_populates="multiple_choice_question")
    answer_options = relationship("AnswerOption", back_populates="question", cascade="all, delete-orphan")
    choice_answers = relationship("ChoiceAnswers", back_populates="choice_question", cascade="all, delete-orphan")

    def __init__(self, questionId, allowMultipleAnswers):
        self.questionId = questionId
        self.allowMultipleAnswers = allowMultipleAnswers

    def serialize(self):
        return {
            'id': self.id,
            'questionId': self.questionId,
            'allowMultipleAnswers': self.allowMultipleAnswers
        }

    def add_question(self):
        session.add(self)
        session.commit()


class AnswerOption(Base):
    __tablename__ = 'answer_options'
    id = Column(Integer, primary_key=True, index=True)
    multiple_choice_questions_id = Column(Integer, ForeignKey(MultipleChoiceQuestion.id), nullable=False)
    text = Column(String(255), nullable=True)
    value_ = Column(String(255), nullable=True)
    defaultValue = Column(Boolean, nullable=True)
    image = Column(MEDIUMBLOB, nullable=True)
    question = relationship("MultipleChoiceQuestion", back_populates="answer_options")
    answer_options_choice_answers = relationship("AnswerOptionsChoiceAnswer", back_populates="answer_option", cascade="all, delete-orphan")

    def __init__(self, multiple_choice_questions_id, text=None, value=None, defaultValue=None,  image=None):
        self.multiple_choice_questions_id = multiple_choice_questions_id
        self.text = text
        self.value_ = value
        self.defaultValue = defaultValue
        self.image = image

    def serialize(self):
        return {
            'id': self.id,
            'multiple_choice_questions_questionId': self.multiple_choice_questions_id,
            'text': self.text,
            'value': self.value_,
            'image': self.image
        }

    @staticmethod
    def answer_options(multiple_choice_questions_id):
        return session.query(AnswerOption).filter_by(multiple_choice_questions_id=multiple_choice_questions_id)

    def add_answer(self):
        session.add(self)
        session.commit()
