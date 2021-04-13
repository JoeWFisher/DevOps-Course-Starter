import pytest
import app
import dotenv
import requests
import mongo
import json
import Item
import os
import datetime
import mongomock
import pymongo

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = dotenv.find_dotenv('.env.test') 
    dotenv.load_dotenv(file_path, override=True)    
    
    test_login = 'True'
    os.environ['LOAD_DISABLED'] = test_login
    
    # Create the new app.     
    test_app = app.create_app()   
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client 

@mongomock.patch(servers=(("mongo", 27017),))    
def test_index_page(client): 
    setup_database()
    response = client.get('/')

    assert 'Test Return' in response.data.decode()


def setup_database():
    client = pymongo.MongoClient(os.environ["Mongo_Url"])
    db = client.get_default_database()
    db.ToDoCollection.insert_one({"last_modified": str(datetime.date.today()), "status": "To Do", "name": "Test Return"})