from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from matplotlib.pyplot import plot
from database.db_config import engine
from models.survey import Survey
from dash import dcc, html, Dash, Input, Output

from app import app
from common.queries import query_multiple_choices, query_open_answers, query_scale_answers
from common.utils import create_dashboards

surveyId = 16

class GetDataSummary(Resource):
    @jwt_required()
    def get(self, survey_id):
        current_user_id = get_jwt_identity()
        survey = Survey.get_survey(survey_id)
        if survey:
            if survey.surveyOwner != current_user_id:
                return {'message': 'You are not allowed to access this survey.'}, 400
            else:
                global surveyId
                surveyId = survey_id
                return {'message': 'Survey answers retrieved successfully.'}, 200
        else:
            return {'message': 'Survey not found.'}, 404

def get_data(surveyId):
    with engine.begin() as connection:
        cursor = connection.execute(query_multiple_choices, (surveyId,))
        choices_answers = cursor.mappings().all()
        cursor = connection.execute(query_open_answers, (surveyId,))
        open_answers = cursor.mappings().all()
        cursor = connection.execute(query_scale_answers, (surveyId,))
        scale_answers = cursor.mappings().all()
    graphs, big_numbers, fig_completion_rate = create_dashboards(choices_answers, open_answers, scale_answers)
    return graphs, big_numbers, fig_completion_rate

graphs, big_numbers, fig_completion_rate = get_data(surveyId)
dashboard_plots = html.Div(id='plots')

dashboard_app = Dash(__name__, server=app, url_base_pathname='/dashboard/')
dashboard_app.layout = html.Div(style={'width': '100%'}, children=[
    dcc.Interval('interval', interval = 1, n_intervals = 0, max_intervals=0),
    dashboard_plots
])

@dashboard_app.callback(Output('plots', 'children'), [Input('interval', 'n_intervals')])
def update_graph(n_intervals):
    graphs, big_numbers, fig_completion_rate = get_data(surveyId)
    children = [html.Div(style={'width': '100%'}, children=[
        html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
            html.H3(children='Summarize', style={'textAlign': 'center'}),
            dcc.Graph(
                id='big-numbers',
                figure=big_numbers
            ),
        ]),
        html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
            html.H3(children='Question Completion Rate', style={
                'textAlign': 'center',
            }),

            dcc.Graph(
                id='example-graph-rate',
                figure=fig_completion_rate
            ),
        ]),
    ]),
    *graphs]
    return children
    