import os

from flask import Flask, render_template
from pymongo import MongoClient

from collection import ChicagoHouseIndex
from database import HouseIndex

app = Flask(__name__)

house_index = HouseIndex()
db = house_index.db

@app.route('/', methods=['GET'])
def index():
    collection = ChicagoHouseIndex(db)
    documents = collection.get_documents()
    return render_template('index.html', cur=list(documents))