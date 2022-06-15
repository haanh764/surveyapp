from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.db_config import engine
from models.survey import Survey
from dash import dcc, html, Dash, dash_table, Input, Output

from app import app
from common.queries import query_multiple_choices, query_open_answers, query_scale_answers
from common.utils import get_statistics, split_filter_part, create_dashboards, PAGE_SIZE

def create_dashboard_view(flask_server, graphs, big_numbers, fig_completion_rate):
    dashboard_app = Dash(__name__, server=flask_server, url_base_pathname='/dashboard/')
    dashboard_app.layout = html.Div(style={'width': '100%'}, children=[
        html.Div(style={'width': '100%'}, children=[
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
        *graphs
    ])
    return dashboard_app

class QueriesSurveyAnswer(Resource):
    @jwt_required()
    def get(self, survey_id):
        current_user_id = get_jwt_identity()
        survey = Survey.get_survey(survey_id) 
        if survey.surveyOwner != current_user_id:
            return {'message': 'You are not allowed to access this survey.'}, 400
        else:
            with engine.begin() as connection:
                cursor = connection.execute(query_multiple_choices, (survey_id,))
                choices_answers = cursor.mappings().all()
                cursor = connection.execute(query_open_answers, (survey_id,))
                open_answers = cursor.mappings().all()
                cursor = connection.execute(query_scale_answers, (survey_id,))
                scale_answers = cursor.mappings().all()

            graphs, big_numbers, fig_completion_rate = create_dashboards(choices_answers, open_answers, scale_answers)
            try:
                create_dashboard_view(app, graphs, big_numbers, fig_completion_rate)
            except Exception as e:
                print(e)
            return  {'message': 'Survey dashboard retrieved successfully.'}, 200

def create_datatable_view(flask_server, df_all_answers):
    dash_datatable_app = Dash(__name__, server=flask_server, url_base_pathname='/datatable/')
    dash_datatable_app.layout = html.Div([
        dash_table.DataTable(
            id='datatable-interactivity',
            columns=[
                {"name": i, "id": i} for i in df_all_answers.columns
            ],
            page_current=0,
            page_size=PAGE_SIZE,
            page_action='custom',

            sort_action='custom',
            sort_mode='multi',
            sort_by=[],

            filter_action='custom',
            filter_query='',

            fixed_columns={'headers': True, 'data': 2},
            style_table={'minWidth': '100%'},
            style_data={'height': 'auto', 'whiteSpace': 'normal',},
            style_cell={'textAlign': 'left'},
        ),
    ],
    style={'width': '80%', 'display': 'inline-block', 'align': 'center'})
    @dash_datatable_app.callback(
        Output('datatable-interactivity', 'data'),
        Input('datatable-interactivity', "page_current"),
        Input('datatable-interactivity', "page_size"),
        Input('datatable-interactivity', 'sort_by'),
        Input('datatable-interactivity', 'filter_query'))
    def update_table(page_current, page_size, sort_by, filter):
        filtering_expressions = filter.split(' && ')
        df = df_all_answers.copy()
        for filter_part in filtering_expressions:
            column_name, operator, filter_value = split_filter_part(filter_part)

            if column_name is not None:
                if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
                    df = df.loc[getattr(df_all_answers[column_name], operator)(filter_value)]
                elif operator == 'contains':
                    df = df.loc[df_all_answers[column_name].str.contains(filter_value)]
                elif operator == 'datestartswith':
                    df = df.loc[df_all_answers[column_name].str.startswith(filter_value)]
                
        if len(sort_by):
            df = df.sort_values(by=[col['column_id'] for col in sort_by], ascending=[
                    col['direction'] == 'asc'
                    for col in sort_by
                ],inplace=False)

        page = page_current
        size = page_size
        return df.iloc[page * size: (page + 1) * size].to_dict('records')
    return dash_datatable_app

class GenrateDataTable(Resource):
    @jwt_required()
    def get(self, survey_id):
        current_user_id = get_jwt_identity()
        survey = Survey.get_survey(survey_id) 
        if survey.surveyOwner != current_user_id:
            return {'message': 'You are not allowed to access this survey.'}, 400
        else:
            with engine.begin() as connection:
                cursor = connection.execute(query_multiple_choices, (survey_id,))
                choices_answers = cursor.mappings().all()
                cursor = connection.execute(query_open_answers, (survey_id,))
                open_answers = cursor.mappings().all()
                cursor = connection.execute(query_scale_answers, (survey_id,))
                scale_answers = cursor.mappings().all()
            
            df_all_answers, question_completion_df, num_respondents, num_questions, completion_rate, questions_list, choice_questions, open_ans_questions, scale_questions = get_statistics(choices_answers, open_answers, scale_answers)
            try:
                create_datatable_view(app, df_all_answers)
            except Exception as e:
                print(e)
            return {'message': 'Survey answers retrieved successfully.'}, 200
