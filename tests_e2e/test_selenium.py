import todo.app as app
import requests as r
import pytest
import os
from threading import Thread
from selenium import webdriver

def createBoard(key, token, boardName):
    resp = r.get(f"https://api.trello.com/1/boards/?key={key}&token={token}&name={boardName}").json()
    return resp['id']

def deleteBoard(key, token, boardId):
    r.delete(f"https://api.trello.com/1/boards/{boardId}?key={key}&token={token}")

@pytest.fixture(scope='module')
def test_app():
    board_id = createBoard('key', 'token', 'testBoard')
    os.environ['TRELLO_BOARD_ID'] = board_id
    
    application = app.create_app()

    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    thread.join(1)
    deleteBoard('key', 'token', board_id)

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

