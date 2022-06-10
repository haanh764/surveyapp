from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.survey import Survey
from models.question import Question, ScaleQuestion, OpenAnswerQuestion, MultipleChoiceQuestion, AnswerOption
from database.db_connector import db_connector

class AddSurvey(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        try:
            config = data['config']
            data = data['data']
            survey = Survey(current_user_id, data['title'], data['description'], config['startDate'], config['endDate'])
            db_connector.add_model_to_db(survey)

            questions = data['formBuilder']['formBuilder']['list']
            for i, question in enumerate(questions):
                options = question['options']
                if isinstance(options, dict) and 'tag' in options:
                    base_question = Question(survey.id, options['defaultValue'],
                                             question['order'], tag=options['tag'])
                    db_connector.add_model_to_db(base_question)
                else:
                    type = question['type']
                    base_question = Question(survey.id, question['question'], question['order'],
                                             description=question['description'])
                    db_connector.add_model_to_db(base_question)
                    if type == 'slider':
                        scale_question = ScaleQuestion(base_question.id, options['min'], options['max'])
                        db_connector.add_model_to_db(scale_question)

                    elif type == 'checkbox' or type == 'radio':
                        allow_multiple_answers = True if type == 'checkbox' else False
                        multiple_choice_question = MultipleChoiceQuestion(base_question.id, allow_multiple_answers)
                        db_connector.add_model_to_db(multiple_choice_question)

                        answers = options['options']
                        for answer in answers:
                            answer_option = AnswerOption(multiple_choice_question.id, answer['text'])
                            db_connector.add_model_to_db(answer_option)
                    elif type == 'input':
                        open_answer_question = OpenAnswerQuestion(base_question.id)
                        db_connector.add_model_to_db(open_answer_question)
        except KeyError:
            return {'message': 'Invalid data in post request.'}, 400
        return {'message': 'The survey {} has been created.'.format(survey.title)}, 200
