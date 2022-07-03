import pandas as pd

from abc import ABC, abstractmethod
from datetime import datetime

class Collection(ABC):

    def __init__(self, db):
        self.db = db
        self.collection = db[self.NAME]

    def create(self):
        if self.NAME not in self.db.list_collection_names():
            self.db.create_collection(self.NAME, validator=self.VALIDATOR)

    def get_documents(self):
        return self.collection.find()

    @abstractmethod
    def update(self):
        pass

class ChicagoHouseIndex(Collection):

    NAME = 'chicago_house_index'
    VALIDATOR = {'$jsonSchema': {
        'bsonType': 'object',
        'required': ['date', 'index'],
        'properties': {
            'date': {
                'bsonType': 'date',
                'description': 'date'
            },
            'index': {
                'bsonType': ['double'],
                'description': 'house index'
            }
        }
    }}
    URL = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=CHXRSA'

    def update(self):
        print('Updating Chicago House Index...')
        self.create()
        df = pd.read_csv(self.URL, header=None)
        for index, row in df.iloc[1: , :].iterrows():
            d = row[0]
            print('Updating index for ' + d + '...')
            dt = datetime.strptime(d, '%Y-%m-%d')
            index = float(row[1])
            key = {'date': dt}
            value = {'index': index}
            self.collection.update_one(key, {'$set': value}, upsert=True)
