from collections.abc import MutableMapping
import plotly.express as px
from neo4j import GraphDatabase
import pandas as pd
import mysql.connector
from pymongo import MongoClient
from neo4j import GraphDatabase
import dash
import plotly.graph_objs as go
from py2neo import Graph
from dash import html
from dash import dcc
import mysql_utils
import mongodb_utils2
import neo4j_utils

# Neo4j Bar Graph for Popular Keywords
bar_graph = neo4j_utils.getBarGraph1()
bar_graph2 = neo4j_utils.getBarGraph2()

app = dash.Dash(__name__, external_stylesheets=["/assets/bootstrap.min.css"],
                external_scripts=["/assets/bootstrap.min.js"])

# Define the Dash layout
app.layout = html.Div([
    # Title
    html.H1("Exploring Publications", style={"text-align": "center"}),

    # Graph of Popular Keywords && Graph of Popular Publications
    html.Div(children=[
        html.Div(bar_graph, style={'display': 'inline-block', 'width': '50%', 'overflow': 'hidden', 'border': '1px solid black',
        'border-radius': '5px'}), 
        html.Div(bar_graph2, style={'display': 'inline-block', 'width': '50%', 'overflow': 'hidden', 'border': '1px solid black',
        'border-radius': '5px'})]),

    # Graph of Popular Publications
    # html.Div(bar_graph2, style={'width': '50%', 'resize': 'none', 'overflow': 'hidden'}),

    # Keyword Search
    html.Div(children=[html.Div([
        html.H2("Search by Keyword", style={"text-align": "center"}),
        dcc.Input(id='input-1', type='text', value='', style={"margin": "auto"}),
        html.Button('Submit', id='submit-button', n_clicks=0, style={"margin": "auto"}),
        html.Br(),
        dcc.Textarea(id='output', style={"margin": "auto", 'width': '100%', 'height': '150px', 'resize': 'none', 'overflowY': 'scroll'}),
    ], style={'padding': '10px', 'display': 'inline-block', 'width': '50%', 'resize': 'none', 'overflow': 'hidden', 'border': '1px solid black',
        'border-radius': '5px'}), 
    # Publication Title Search
    html.Div([
        html.H2("Get All Keywords by Title", style={"text-align": "center"}),
        dcc.Input(id='input-4', type='text', value='', style={"margin": "auto"}),
        html.Button('Submit', id='submit-button4', n_clicks=0, style={"margin": "auto"}),
        html.Br(),
        dcc.Textarea(id='output4', style={"margin": "auto", 'width': '100%', 'height': '150px', 'resize': 'none', 'overflowY': 'scroll'}),
    ], style={'padding': '10px', 'display': 'inline-block', 'width': '50%', 'resize': 'none', 'overflow': 'hidden', 'border': '1px solid black',
        'border-radius': '5px'})]),

    # Add Publication
    html.Div(children=[html.Div([html.H2("Edit Publication Name", style={"text-align": "left"}),
    dcc.Input(
        id='input-3',
        type='text',
        value='Prior publication name, new publication name'
    ),
    html.Button('Submit', id='submit-button3', n_clicks=0),
    html.Div(id='output3')], style={'padding': '10px', 'display': 'inline-block', 'width': '50%', 'resize': 'none', 'overflow': 'hidden', 'border': '1px solid black',
        'border-radius': '5px'}),
    html.Div([# Edit Keyword
    html.H2("Edit Keyword", style={"text-align": "left"}),
    dcc.Input(
        id='input-2',
        type='text',
        value='PreviousKeywordName,NewKeywordName'
    ),
    html.Button('Submit', id='submit-button2', n_clicks=0),
    html.Div(id='output2')], style={'padding': '10px', 'display': 'inline-block', 'width': '50%', 'resize': 'none', 'overflow': 'hidden', 'border': '1px solid black',
        'border-radius': '5px'})
    ]),
    html.Div(children=[html.H2("Get Publication Count"), html.Button('GO', id='submit-button6', n_clicks=0), html.Div(id='output6')]),
])

# Queries by Keyword, Returns Publications Matched
@app.callback(
    dash.dependencies.Output('output', "value"),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('input-1', 'value')])
def update_output(n_clicks, value):
    keyword = "{}".format(value)
    str = mysql_utils.getPublications(keyword)
    return str

# Queries by Title, Returns Keywords
@app.callback(
    dash.dependencies.Output('output4', "value"),
    [dash.dependencies.Input('submit-button4', 'n_clicks')],
    [dash.dependencies.State('input-4', 'value')])
def update_output(n_clicks, value):
    keyword = "{}".format(value)
    str = mongodb_utils2.getKeywords(keyword)
    return str

# Edits Publication Name
@app.callback(
    dash.dependencies.Output('output3', "children"),
    [dash.dependencies.Input('submit-button3', 'n_clicks')],
    [dash.dependencies.State('input-3', 'value')])
def update_output(n_clicks, value):
    # Prepared Statement (R11)
    keyword = "{}".format(value)
    str = mysql_utils.editPublicationName(keyword)
    return "{}".format(str)

# Edit Keyword Name
@app.callback(
    dash.dependencies.Output('output2', "children"),
    [dash.dependencies.Input('submit-button2', 'n_clicks')],
    [dash.dependencies.State('input-2', 'value')])
def update_output(n_clicks, value):
    keyword = "{}".format(value)
    str = mysql_utils.editKeywordName(keyword)
    return str

# Adds a Keyword for a Publication
@app.callback(
    dash.dependencies.Output('output6', 'children'),
    [dash.dependencies.Input('submit-button6', 'n_clicks')])
def update_output(n_clicks):
    str = mysql_utils.getNumberOfPublications()
    return str.translate(str.maketrans("", "", "()[]"))

if __name__ == '__main__':
    app.run_server(debug=True)