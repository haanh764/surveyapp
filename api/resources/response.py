from flask import jsonify, request
from flask_restful import Resource, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_mail import Message
from app import mail


from models.survey import Survey, Respondents, Responses, Answers, OpenAnswers, ScaleAnswers, ChoiceAnswers, AnswerOptionsChoiceAnswer
from models.respondents import AllowedRespondents
from models.user import User
from models.question import Question, ScaleQuestion, OpenAnswerQuestion, MultipleChoiceQuestion, AnswerOption
from email_validator import validate_email, EmailNotValidError

from resources.survey import is_allowed, is_email_valid


class AddResponse(Resource):
    @jwt_required(optional=True)
    def post(self, survey_id):
        data = request.get_json()
        survey = Survey.get_survey(survey_id)
        isOwner = False
        user_email = None
        try:
            current_user_id = get_jwt_identity()
            if current_user_id is not None:
                if not is_allowed(User.find_by_id(current_user_id)):
                    return {'message': 'You are not allowed to access the website.'}, 403
                if survey.surveyOwner == current_user_id:
                    isOwner = True
            user_email = User.find_by_id(current_user_id).email
        except Exception:
            isOwner = False
        if ((survey.isPublic or data['surveyToken'] == survey.surveyHash) and survey.is_published()) or (survey.is_published() and isOwner):
            email = data['email']
            respondent_id = None
            if not email and user_email is not None:
                email = user_email
            if email and is_email_valid(email):
                respondent = Respondents.get_respondent(email)
                if respondent is None or not respondent:
                    respondent = Respondents(email)
                    respondent.add_respondent()
                respondent_id = respondent.id
            response = Responses(respondent_id, survey_id)
            response.add_response()
            for reponse_item in data['responseItems']:
                model = reponse_item['questionModel']
                if not model.startswith('text'):
                    base_question = Question.get_question(model)
                    answerValue = reponse_item['answerValue']
                    answer = Answers(response.id)
                    if model.startswith('slider'):
                        question = base_question.scale_question[0]
                        if answerValue >= question.min_value and answerValue <= question.max_value:
                            answer.add_answer()
                            s_answer = ScaleAnswers(answer.id, question.id, answerValue)
                            s_answer.add_answer()
                        pass
                    elif model.startswith('radio'):
                        question = base_question.multiple_choice_question[0]
                        answer_options = AnswerOption.answer_options(question.id)
                        for a_o in answer_options:
                            if a_o.value_ == answerValue:
                                answer.add_answer()
                                choice_answer = ChoiceAnswers(answer.id, question.id)
                                choice_answer.add_answer()
                                a_o_c_a = AnswerOptionsChoiceAnswer(choice_answer.id, a_o.id)
                                a_o_c_a.add_answer()
                                break
                        pass
                    elif model.startswith('checkbox'):
                        question = base_question.multiple_choice_question[0]
                        answer_options = AnswerOption.answer_options(question.id)
                        first_answer = True
                        choice_answer = None
                        for a_v in list(set(answerValue)):
                            for a_o in answer_options:
                                if a_o.value_ == a_v:
                                    if first_answer:
                                        answer.add_answer()
                                        choice_answer = ChoiceAnswers(answer.id, question.id)
                                        first_answer = False
                                        choice_answer.add_answer()
                                    a_o_c_a = AnswerOptionsChoiceAnswer(choice_answer.id, a_o.id)
                                    a_o_c_a.add_answer()
                                    break
                        pass
                    elif model.startswith('input'):
                        question = base_question.open_answer_question[0]
                        answer.add_answer()
                        o_answer = OpenAnswers(answer.id, question.id, answerValue)
                        o_answer.add_answer()
            return {'message': 'The response has been saved.'}, 200
        else:
            return {'message': 'You are not allowed to perform this action.'}, 400