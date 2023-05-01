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

def getKeywords(keyword):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['academicworld']
    collection = db['publications']
    monres = collection.find({ "title": keyword })
    str = ""
    for doc in monres:
        print(doc)
        for k in doc['keywords']:
            str += "{}".format(k['name']) + "\n"
    if str == "":
        return ""
    return str