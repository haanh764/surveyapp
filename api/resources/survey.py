from flask import jsonify, request
from flask_restful import Resource, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_mail import Message
from app import mail


from models.survey import Survey, Respondents
from models.respondents import AllowedRespondents
from models.user import User
from models.question import Question, ScaleQuestion, OpenAnswerQuestion, MultipleChoiceQuestion, AnswerOption
from email_validator import validate_email, EmailNotValidError


def is_allowed(user):
    return user.isActivated and not user.isBlocked


def is_email_valid(email):
    try:
        email = validate_email(email).email
        return True
    except EmailNotValidError:
        return False


def send_email(to, subject, sender, confirm_url):
    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = 'A survey from {} is here: {}'.format(sender, confirm_url)
    mail.send(msg)


class AddSurvey(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        if not is_allowed(User.find_by_id(current_user_id)):
            return {'message': 'User is not allowed to perform this action.'}, 400
        try:
            config = data['config']
            data = data['data']
            exists = False
            if 'id' in data:
                survey = Survey.get_survey(data['id'])
                if not survey:
                    return {'message': 'Id is passed but no survey with such id exists.'}, 400
                if not survey.surveyOwner == current_user_id:
                    return {'message': 'User is not the owner of this survey.'}, 400
                exists = True
            else:
                survey = Survey(current_user_id, data['title'], data['description'], config['startDate'], config['endDate'], config['isPublic'])
            if exists:
                survey.modify(data['title'], data['description'], config['startDate'], config['endDate'], config['isPublic'])
                for question in survey.questions:
                    question.delete_question()
            survey.add_survey()
            questions = data['formBuilder']['list']
            for i, question in enumerate(questions):
                options = question['options']
                model_key = question['key']
                model = question['model']
                if isinstance(options, dict) and 'tag' in options:
                    base_question = Question(survey.id, question['title'],
                                             question['order'], tag=options['tag'],
                                             model_key=model_key, model=model,
                                             defaultValue=options['defaultValue'])
                    base_question.add_question()
                else:
                    type = question['type']
                    base_question = Question(survey.id, question['title'], question['order'],
                                             description=question['description'],
                                             model_key=model_key, model=model)
                    base_question.add_question()
                    if type == 'slider':
                        scale_question = ScaleQuestion(base_question.id, options['min'], options['max'], options['defaultValue'], options['step'])
                        scale_question.add_question()
                    elif type == 'checkbox' or type == 'radio':
                        allow_multiple_answers = True if type == 'checkbox' else False
                        multiple_choice_question = MultipleChoiceQuestion(base_question.id, allow_multiple_answers)
                        multiple_choice_question.add_question()
                        answers = options['options']
                        for i, answer in enumerate(answers):
                            default_value = False
                            if type == 'radio':
                                if i == options['defaultValue']:
                                    default_value = True
                            else:
                                if i in options['defaultValue']:
                                    default_value = True
                            answer_option = AnswerOption(multiple_choice_question.id, answer['text'], answer['value'], default_value)
                            answer_option.add_answer()

                    elif type == 'input':
                        open_answer_question = OpenAnswerQuestion(base_question.id, options['defaultValue'], options['placeholder'])
                        open_answer_question.add_question()
        except KeyError:
            return {'message': 'Invalid data in post request.'}
        emails = config['emails']
        emails = list(set(emails))
        for email in emails:
            respondent = Respondents.get_respondent(email)
            if respondent is None or not respondent:
                respondent = Respondents(email)
                respondent.add_respondent()
            allowed_respondent = AllowedRespondents(respondent.id, survey.id)
            allowed_respondent.add_allowed_respondent()
        if config['isSurveySentAutomatically']:
            user = User.find_by_id(current_user_id)
            sender = user.email
            #link = url_for('getsurvey', survey_id=survey.id, hash=survey.surveyHash, _external=True)
            link = 'localhost:8001/#/survey/' + str(survey.id) + '?hash=' + survey.surveyHash
            for email in emails:
                if is_email_valid:
                    send_email(email, 'You have been assigned to a new survey.', sender, link)
        if exists:
            return {'message': 'The survey {} has been modified.'.format(survey.title)}, 200
        return {'message': 'The survey {} has been created.'.format(survey.title)}, 200


class ListSurveysByUser(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        surveys = Survey.list_surveys_by_user(current_user_id)
        return jsonify([survey.serialize() for survey in surveys])


class GetSurvey(Resource):
    def get(self, survey_id):
        allow = False
        survey = Survey.get_survey(survey_id)
        surveyHash = request.args.get('hash', None)
        if not survey:
            return {'message': 'Such survey does not exist.'}, 403
        if survey.isPublic:
            allow = True
        else:
            if surveyHash is not None:
                if surveyHash == survey.surveyHash:
                    allow = True
        if not allow:
            return {'message': 'You are not allowed to access this survey.'}, 403
        survey_json = survey.get_json()
        return jsonify(survey_json)
