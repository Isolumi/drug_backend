from . import mongo
from models.medication import Medication

def check_connection():
    try:
        mongo.client.admin.command('ping')
        print('Connected to MongoDB')
    except Exception as e:
        print(f'Error: {e}')
    
def add_item(data):
    return mongo.db.medications.insert_one(data.model_dump())

def test():
    medication = Medication(
        name='bandana',
        date_received='2021-01-01',
        num_refills=1,
        duration=1
    )
    print(medication.model_dump_json())
    return medication