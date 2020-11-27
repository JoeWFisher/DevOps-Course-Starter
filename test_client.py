import pytest
import app
import dotenv
import requests
import trello
import json
import Item
import os
import datetime

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = dotenv.find_dotenv('.env.test') 
    dotenv.load_dotenv(file_path, override=True)    
    
    # Create the new app.     
    test_app = app.create_app()   
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client 

@pytest.fixture
def mock_get_request(monkeypatch):

    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = 'http://test'
            self.headers = {'blaa': '1234'}
        
        def json(self):
            return [{"id": "1", "dateLastActivity": str(datetime.date.today()), "idList": os.environ['ToDoId'], "name": "Test Return"}]

    def mock_response(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_response)
    
def test_index_page(mock_get_request, client): 
    response = client.get('/')

    assert 'Test Return' in response.data.decode()

