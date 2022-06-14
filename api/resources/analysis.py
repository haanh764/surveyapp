from flask_restful import Resource
from flask import jsonify, request
import flask
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.db_config import engine
from models.survey import Survey
from dash import dcc, html, Dash
import plotly.express as px
from app import app

class QueriesSurveyAnswer(Resource):
    # @jwt_required()
    def post(self):
        data = request.get_json()
        # current_user_id = get_jwt_identity()
        survey_id = data['survey_id']
        # selected_survey = Survey.get_survey(survey_id=survey_id)
        # if selected_survey.surveyOwner != current_user_id:
            # return {'message': 'You are not allowed to access this survey.'}, 400
        # else:
        query = "SELECT responses.id, respondents.email, questions.title, answer_options.text \
                FROM choice_answers JOIN answer_options_choice_answer ON choice_answers.id = answer_options_choice_answer.choice_answerId \
                JOIN multiple_choice_questions ON multiple_choice_questions.id = choice_answers.multiple_choice_questionsId \
                JOIN questions ON questions.id = multiple_choice_questions.questionId \
                JOIN answer_options ON answer_options.id = answer_options_choice_answer.answer_optionId \
                JOIN answers ON answers.id = choice_answers.answerId \
                JOIN responses ON answers.responseId = responses.id \
                JOIN respondents ON responses.respondentId = respondents.id \
                JOIN surveys ON surveys.id = responses.surveyId \
                WHERE surveys.id = %s"
        with engine.begin() as connection:
            cursor = connection.execute(query, (survey_id,))
            result = cursor.mappings().all()
        print(result)

        df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
        df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
        fig = px.pie(df, values='pop', names='country', title='Population of European continent')
        dash_app = Dash(__name__, server=app, url_base_pathname='/dash/test1/')
        dash_app.layout = html.Div([
            dcc.Graph(
                id='example-graph',
                figure=fig)
        ])
        if __name__ == '__main__':
            dash_app.run_server(debug=True)
        return  {'message': 'Survey answers retrieved successfully.'}, 200
