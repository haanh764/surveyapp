from sqlalchemy import Column, Integer, String, ForeignKey
from database.db_config import Base, session
from sqlalchemy.orm import relationship
from models.survey import Survey
from models.responses import Responses
from models.question import Question, ScaleQuestion, OpenAnswerQuestion, MultipleChoiceQuestion, AnswerOption


class Responses(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True, index=True)
    respondentId = Column(Integer, ForeignKey(Respondents.id), nullable=False)
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

    @staticmethod
    def get_responses(surveyId):
        return session.query(AllowedRespondents).filter_by(surveyId=surveyId)


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    responseId = Column(Integer, ForeignKey(Respondents.id), nullable=False)
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
    scale_answer_question_id = Column(Integer, ForeignKey(ScaleQuestion.id), nullable=False)
    scale_question = relationship("ScaleQuestion", back_populates="scale_answers")
    value = Column(Integer, nullable=False)

    def __init__(self, answerId, scale_answer_question_id, value):
        self.answerId = answerId
        self.scale_answer_question_id = scale_answer_question_id
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
    choiceAnswersId = Column(Integer, ForeignKey(ChoiceAnswers.id), nullable=False)
    choiceAnswer = relationship("ChoiceAnswers", back_populates="answer_options_choice")
    answer_optionId = Column(Integer, ForeignKey(AnswerOption.id), nullable=False)
    answer_option = relationship("AnswerOption", back_populates="answer_options_choice_answers")

    def __init__(self, choiceAnswersId, answer_optionId):
        self.choiceAnswersId = choiceAnswersId
        self.answer_optionId = answer_optionId

    def add_answer(self):
        session.add(self)
        session.commit()
