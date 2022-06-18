import pandas as pd
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from wordcloud import WordCloud

DATATABLE_OPERATORS = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]
PAGE_SIZE = 10

def result_processed(results):
    df = pd.DataFrame(results, columns=list(results[0].keys()))
    keys = df.columns.to_list()
    grouped_df = df.groupby(keys[:-1])[keys[-1]].apply(lambda x: ', '.join(x.astype(str))).reset_index()
    pivot_df = grouped_df.set_index(['id','email', 'title'], drop=True).unstack('title')
    pivot_df.columns = pivot_df.columns.droplevel(0)
    return pivot_df

def get_statistics(choice_ans, open_ans, scale_ans):
    df_choices_answers = result_processed(choice_ans)
    df_open_answers = result_processed(open_ans)
    df_scale_answers = result_processed(scale_ans)

    choice_questions = df_choices_answers.columns.to_list()
    open_ans_questions = df_open_answers.columns.to_list()
    scale_questions = df_scale_answers.columns.to_list()

    df_all_answers = pd.concat([df_choices_answers, df_open_answers, df_scale_answers], axis=1)
    df_all_answers.columns.name=''
    df_all_answers = df_all_answers.reset_index()
    for column in df_all_answers.columns:
        try:
            df_all_answers[column] = df_all_answers[column].astype(int)
        except:
            print('Cant convert to type int')

    questions_list = df_all_answers.columns[2:].to_list()
    num_respondents = len(df_all_answers.email.unique())
    num_questions = len(df_all_answers.columns[2:])
    completion_rate = 100 - df_all_answers.isnull().sum().sum()/(num_questions*num_respondents)*100

    question_completion_rates = 100 - (df_all_answers[questions_list].isnull().sum()/num_respondents)*100
    question_completion_df = question_completion_rates.to_frame()
    question_completion_df.columns = ['Completion Rate']

    return df_all_answers, question_completion_df, num_respondents, num_questions, completion_rate, questions_list, choice_questions, open_ans_questions, scale_questions

def split_filter_part(filter_part):
    for operator_type in DATATABLE_OPERATORS:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part
                return name, operator_type[0].strip(), value
    return [None] * 3

def create_dashboards(choices_answers, open_answers, scale_answers):
    df_all_answers, question_completion_df, num_respondents, num_questions, completion_rate, questions_list, choice_questions, open_ans_questions, scale_questions = get_statistics(choices_answers, open_answers, scale_answers)
    fig_completion_rate = px.bar(question_completion_df, y='Completion Rate', height=600, text='Completion Rate',)
    fig_completion_rate.update_traces(marker_color='#e8795a', width=0.5, texttemplate='%{text:.2s} %', textposition='outside')

    data_type_df = pd.DataFrame(df_all_answers[df_all_answers.columns[2:]].dtypes, columns=['Data_Type'])
    num_numerical_data = data_type_df[data_type_df['Data_Type'] == int].shape[0]
    num_categorical_data = len(choice_questions)
    num_textual_data = num_questions - num_numerical_data - num_categorical_data
    graphs = []

    for idx, col in enumerate(df_all_answers.columns[2:]):
        if col in choice_questions:
            if df_all_answers[col].apply(lambda x: len(str(x).split(','))).value_counts().shape[0] >= 2:
                fig = px.bar(df_all_answers[col].str.get_dummies(sep=', ').sum(), height=600, title=f'<b>Question {idx}. {col}</b>')
                fig.update_traces(marker_color='#e8795a', width=0.5)
                graphs.append(dcc.Graph(
                    id=f'example-graph-{idx}',
                    figure=fig
                ))
            else:
                if len(df_all_answers[col].unique()) < 5:
                    count_df = pd.DataFrame(df_all_answers[col].value_counts())
                    fig = px.pie(count_df, values=col, names=count_df.index.to_list(), color_discrete_sequence=px.colors.sequential.Agsunset, height=600, title=f'<b>Question {idx}. {col}</b>')
                else:
                    fig = px.bar(df_all_answers[col].value_counts(), height=600, title=f'<b>Question {idx}. {col}</b>')
                    fig.update_traces(marker_color='#e8795a', width=0.5)
                graphs.append(dcc.Graph(
                    id=f'example-graph-{idx}',
                    figure=fig
                ))
        elif col in scale_questions:
            fig = px.bar(df_all_answers[col].value_counts(), height=600, title=f'<b>Question {idx}. {col}</b>')
            fig.update_traces(marker_color='#e8795a', width=0.5)
            graphs.append(dcc.Graph(
                id=f'example-graph-{idx}',
                figure=fig
            ))
        elif col in open_ans_questions:
            if df_all_answers[col].dtype=='int64':
                fig = px.box(df_all_answers[col], height=600, title=f'<b>Question {idx}. {col}</b>')
                graphs.append(dcc.Graph(
                    id=f'example-graph-{idx}',
                    figure=fig
                ))
            else:
                wordcloud = WordCloud (
                                    background_color = 'white',
                                    width = 512,
                                    height = 384
                                        ).generate(' '.join(df_all_answers[col]))
                fig = px.imshow(wordcloud)
                fig.update_layout(title=f'<b>Question {idx}. {col}</b>')
                graphs.append(dcc.Graph(
                    id=f'example-graph-{idx}',
                    figure=fig
                ))

    big_numbers = make_subplots(
        rows=3,
        cols=2,
        subplot_titles=('Respondents', 'Questions', 'Completion','Textual data', 'Numerical data', 'Categorical data'),
        specs=[[{'type': 'indicator'}, {'type': 'indicator'}], [{'type': 'indicator'},
    {'type': 'indicator'}], [{'type': 'indicator'}, {'type': 'indicator'}]]
    )

    big_numbers.add_trace(
        go.Indicator(mode="number", value=num_respondents, number={'font_color':'#303972', 'font_size':36}),
        row=1,
        col=1,
    )

    big_numbers.add_trace(
        go.Indicator(mode="number", value=num_questions, number={'font_color':'#303972', 'font_size':36}),
        row=1,
        col=2,
    )

    big_numbers.add_trace(
        go.Indicator(mode="number", value=completion_rate, number = {'suffix': "%", 'font_color':'#303972', 'font_size':36},),
        row=2,
        col=1,
    )

    big_numbers.add_trace(
        go.Indicator(mode="number", value=num_textual_data, number={'font_color':'#303972', 'font_size':36}),
        row=2,
        col=2,
    )

    big_numbers.add_trace(
        go.Indicator(mode="number", value=num_numerical_data, number={'font_color':'#303972', 'font_size':36}),
        row=3,
        col=1,
    )

    big_numbers.add_trace(
        go.Indicator(mode="number", value=num_categorical_data, number={'font_color':'#303972', 'font_size':36}),
        row=3,
        col=2,
    )

    big_numbers.layout.annotations[0].update(yanchor='bottom', y=0.7)
    big_numbers.layout.annotations[1].update(yanchor='bottom', y=0.7)
    big_numbers.layout.annotations[2].update(yanchor='bottom', y=0.3)
    big_numbers.layout.annotations[3].update(yanchor='bottom', y=0.3)
    big_numbers.layout.annotations[4].update(yanchor='bottom', y=-0.1)
    big_numbers.layout.annotations[5].update(yanchor='bottom', y=-0.1)

    return graphs, big_numbers, fig_completion_rate
    