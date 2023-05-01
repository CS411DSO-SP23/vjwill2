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

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="test_root",
database="academicworld"
)
mycursor = mydb.cursor()


def getPublications(keyword):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test_root",
    database="academicworld"
    )
    mycursor = mydb.cursor()
    # Create View (R10)
    mycursor.execute("DROP VIEW publicationview")
    mycursor.execute("CREATE VIEW publicationview AS SELECT p.title, k.name FROM publication p inner join publication_keyword pk on p.id = pk.publication_id inner join keyword k on pk.keyword_id = k.id ORDER BY p.num_Citations")
    query = "SELECT title FROM publicationview WHERE name = '" + keyword + "'"
    mycursor.execute(query)
    results = mycursor.fetchall()
    if not results:
        return ""
    str = ""
    for title, in results: 
        str += title + "\n"
    mydb.close()
    return str

def editPublicationName(keyword):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test_root",
    database="academicworld"
    )
    mycursor = mydb.cursor()
    # Prepared SQL Statement (R11)
    preparedsql = "SELECT p.id FROM publication p WHERE p.title = %s"
    v1, v2 = keyword.split(",")
    print(v1)
    if (keyword != "Prior publication name, new publication name") :
        mycursor.execute(preparedsql, [v1])
        results = mycursor.fetchall()
        id = str(results[0][0])
        statement = "UPDATE publication SET title = '" + v2 + "' WHERE id = " + id
        mycursor.execute(statement)
    else:
        mydb.close()
        return ""
    mydb.close()
    return "success"

def editKeywordName(keyword):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test_root",
    database="academicworld"
    )
    mycursor = mydb.cursor()
    # Prepared SQL Statement (R11)
    preparedsql = "SELECT k.id FROM keyword k WHERE k.name = %s"
    v1, v2 = keyword.split(",")
    if (keyword != "PreviousKeywordName,NewKeywordName") :
        mycursor.execute(preparedsql, [v1])
        results = mycursor.fetchall()
        id = str(results[0][0])
        statement = "UPDATE keyword SET name = '" + v2 + "' WHERE id = " + id
        mycursor.execute(statement)
    else:
        mydb.close()
        return ""
    mydb.close()
    return "success"

def getNumberOfPublications():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test_root",
    database="academicworld"
    )
    mycursor = mydb.cursor()
    # Stored Procedure (R12)
    statement = "CALL getCount()"
    mycursor.execute(statement)
    results = mycursor.fetchall()
    str = "{}".format(results)
    mydb.close()
    return str

def stopSQL():
    mydb.close()