import os
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class MongoDB:
    def __init__(self):
        password = quote_plus(os.getenv('MONGO_PASS'))
        uri = 'mongodb+srv://isolumi:' + password + '@medicine-organizer.yq45ftm.mongodb.net/?retryWrites=true&w=majority&appName=medicine-organizer'
        self.client = MongoClient(uri)
        self.db = self.client['medication-organiser']

        # self.db = self.client[db_name]
        
        
mongo = MongoDB()