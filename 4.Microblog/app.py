import datetime
from flask import Flask, render_template, request # type: ignore
from pymongo import MongoClient # type: ignore

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://<user>:<password>@<mongodb-server>/microblog")
    app.db = client.microblog

    return app
