import os

from flask import Flask, render_template
from pymongo import MongoClient

from collection import ChicagoHouseIndex
from database import HouseIndex

app = Flask(__name__)

db = HouseIndex().db

@app.route('/', methods=['GET'])
def index():
    collection = ChicagoHouseIndex(db)
    documents = collection.get_documents()
    return render_template('index.html', cur=list(documents))