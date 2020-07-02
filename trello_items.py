import requests
from trello_config import KEY, TOKEN, BOARD, PENDING, DONE
import json
from flask import session  

class Item:
    def __init__(self, id, name, list_id):
        self.id = id
        self.title = name
        if list_id == PENDING:
            self.status = 'Not Started'
        elif list_id == DONE:
            self.status = 'Completed'

def get_items():
    response = requests.get('https://api.trello.com/1/boards/{id}/cards?key={key}&token={token}'.format(id=BOARD, key=KEY, token=TOKEN))
    all_items = [Item(item['id'], item['name'], item['idList']) for item in response.json()]
    return all_items

def get_item(id):
    items = get_items()
    return next((item for item in items if item.id == id), None)

def add_item(title):
    requests.post('https://api.trello.com/1/cards?key={key}&token={token}&idList={listId}&name={name}'.format(key=KEY, token=TOKEN, listId=PENDING, name=title))
    return title

def save_item(item):
    if item.status == 'Not Started':
        list_id = PENDING
    elif item.status == 'Completed':
        list_id = DONE
    requests.put('https://api.trello.com/1/cards/{id}?key={key}&token={token}&name={name}&idList={listId}'.format(id=item.id, key=KEY, token=TOKEN, name=item.title, listId=list_id))
    return

def toggle_status(id):
    item = get_item(id)
    if item.status == 'Not Started':
        item.status = 'Completed'
    elif item.status == 'Completed':
        item.status = 'Not Started'
    save_item(item)

def delete_item(id):
    requests.delete('https://api.trello.com/1/cards/{id}?key={key}&token={token}'.format(id=id, key=KEY, token=TOKEN))   
    return