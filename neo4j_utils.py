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

def getBarGraph1():
    # Neo4J Configuration here
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "Fractalterrain66"
    driver = GraphDatabase.driver(uri, auth=(user, password))
    database_name = "academicworld"
    with driver.session(database=database_name) as session:
        neoresult = session.run("MATCH (:INSTITUTE)-[:AFFILIATION_WITH]-(:FACULTY)-[:PUBLISH]->(:PUBLICATION)-[:LABEL_BY]->(k:KEYWORD) WITH k.name AS keyword, COUNT(*) AS keyword_count ORDER BY keyword_count DESC LIMIT 10 RETURN keyword, keyword_count")
        x_values = [r['keyword'] for r in neoresult]
        neoresult = session.run("MATCH (:INSTITUTE)-[:AFFILIATION_WITH]-(:FACULTY)-[:PUBLISH]->(:PUBLICATION)-[:LABEL_BY]->(k:KEYWORD) WITH k.name AS keyword, COUNT(*) AS keyword_count ORDER BY keyword_count DESC LIMIT 10 RETURN keyword, keyword_count")
        y_values = [r['keyword_count'] for r in neoresult]

    # Neo4j Bar Graph for Popular Keywords
    bar_graph = dcc.Graph(
        id='bar-graph',
        figure={
            'data': [
                {'x': x_values, 'y': y_values, 'type': 'bar'}
            ],
            'layout': {
                'title': 'Popular Keywords',
                'xaxis': {'title': 'Keyword'},
                'yaxis': {'title': 'Count'}
            }
        }
    )
    session.close()
    driver.close()
    return bar_graph

def getBarGraph2():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "Fractalterrain66"
    driver = GraphDatabase.driver(uri, auth=(user, password))
    database_name = "academicworld"
    with driver.session(database=database_name) as session:
        neoresult = session.run("MATCH (:INSTITUTE)-[:AFFILIATION_WITH]-(:FACULTY)-[:PUBLISH]->(p:PUBLICATION)-[:LABEL_BY]->(k:KEYWORD) WITH p.title AS publication, COUNT(*) AS citation_count ORDER BY citation_count DESC LIMIT 10 RETURN publication, citation_count")
        x_values = [r['publication'] for r in neoresult]
        neoresult = session.run("MATCH (:INSTITUTE)-[:AFFILIATION_WITH]-(:FACULTY)-[:PUBLISH]->(p:PUBLICATION)-[:LABEL_BY]->(k:KEYWORD) WITH p.title AS publication, COUNT(*) AS citation_count ORDER BY citation_count DESC LIMIT 10 RETURN publication, citation_count")
        y_values = [r['citation_count'] for r in neoresult]

    # Neo4j Bar Graph for Popular Publications
    bar_graph2 = dcc.Graph(
        id='bar-graph2',
        figure={
            'data': [
                {'x': x_values, 'y': y_values, 'type': 'bar'}
            ],
            'layout': {
                'title': 'Popular Publications',
                'xaxis': {'title': 'Publication'},
                'yaxis': {'title': 'Number of Citations'}
            }
        }
    )
    session.close()
    driver.close()
    return bar_graph2