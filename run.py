from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
import certifi
import os
from dotenv import load_dotenv

load_dotenv()


password = quote_plus(os.getenv('MONGO_PASS'))
passs = quote_plus('1@XDaumisomDX')
print(password)
print(passs)
uri = 'mongodb+srv://isolumi:' + passs + '@medicine-organizer.yq45ftm.mongodb.net/?retryWrites=true&w=majority&appName=medicine-organizer'


# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)