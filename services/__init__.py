import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import certifi

load_dotenv()

class MongoDB:
    def __init__(self):
        password = quote_plus(os.getenv('MONGO_PASS'))
        uri = 'mongodb+srv://isolumi:' + password + '@medicine-organizer.yq45ftm.mongodb.net/?retryWrites=true&w=majority&appName=medicine-organizer'
        self.client = MongoClient(uri, tlsCAFile=certifi.where())
        self.db = self.client['medication-organiser']      
        
mongo = MongoDB()