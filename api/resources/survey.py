from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.survey import Survey
from models.question import Question, ScaleQuestion, OpenAnswerQuestion, MultipleChoiceQuestion, AnswerOption


class AddSurvey(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        try:
            config = data['config']
            data = data['data']
            survey = Survey(current_user_id, data['title'], data['description'], config['startDate'], config['endDate'])
            survey.add_survey()
            questions = data['formBuilder']['list']
            for i, question in enumerate(questions):
                options = question['options']
                model_key = question['key']
                model = question['model']
                if isinstance(options, dict) and 'tag' in options:
                    base_question = Question(survey.id, question['title'],
                                             question['order'], tag=options['tag'],
                                             model_key=model_key, model=model)
                    base_question.add_question()
                else:
                    type = question['type']
                    base_question = Question(survey.id, question['title'], question['order'],
                                             description=question['description'],
                                             model_key=model_key, model=model)
                    base_question.add_question()
                    if type == 'slider':
                        scale_question = ScaleQuestion(base_question.id, options['min'], options['max'])
                        scale_question.add_question()
                    elif type == 'checkbox' or type == 'radio':
                        allow_multiple_answers = True if type == 'checkbox' else False
                        multiple_choice_question = MultipleChoiceQuestion(base_question.id, allow_multiple_answers)
                        multiple_choice_question.add_question()
                        answers = options['options']
                        for answer in answers:
                            answer_option = AnswerOption(multiple_choice_question.id, answer['text'])
                            answer_option.add_answer()
                    elif type == 'input':
                        open_answer_question = OpenAnswerQuestion(base_question.id)
                        open_answer_question.add_question()
        except KeyError:
            return {'message': 'Invalid data in post request.'}, 400
        return {'message': 'The survey {} has been created.'.format(survey.title)}, 200

class ListSurveysByUser(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        surveys = Survey.list_surveys_by_user(current_user_id)
        return jsonify([survey.serialize() for survey in surveys])

class GetSurvey(Resource):
    @jwt_required()
    def get(self, survey_id):
        current_user_id = get_jwt_identity()
        survey = Survey.get_survey(survey_id)
        if survey.surveyOwner == current_user_id:
            return jsonify(survey.serialize())
        else:
            return {'message': 'You are not allowed to access this survey.'}, 403
