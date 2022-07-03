import os

from abc import ABC, abstractmethod
from dotenv import dotenv_values
from pymongo import MongoClient

from collection import ChicagoHouseIndex

class Database(ABC):

    def __init__(self):
        #config = dotenv_values(".env")
        #uri = config['MONGODB_URI']
        client = MongoClient('mongodb+srv://beinanwang:denkensolutionscanada@cluster0.rgvpjbi.mongodb.net/?retryWrites=true&w=majority')
        self.db = client[self.NAME]
        print(self.db.list_collection_names())

class HouseIndex(Database):

    NAME = 'house_index'

    def update(self):
        print('Updating house index database...')
        self.update_chicago_house_index()

    def update_chicago_house_index(self):
        collection = ChicagoHouseIndex(self.db)
        collection.update()
