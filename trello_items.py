import requests
from trello_config import KEY, TOKEN, BOARD, PENDING, DONE
import json
from flask import session  


def get_items():
    items = []

    pending_items = requests.get('https://api.trello.com/1/lists/{list_id}/cards?key={key}&token={token}'.format(list_id=PENDING, key=KEY, token=TOKEN))
    for item in pending_items.json():
        items.append({'id':item["id"], 'status':'Not Started', 'title':item["name"]})

    done_items = requests.get('https://api.trello.com/1/lists/{list_id}/cards?key={key}&token={token}'.format(list_id=DONE, key=KEY, token=TOKEN))
    for item in done_items.json():
        items.append({'id':item["id"], 'status':'Completed', 'title':item["name"]})

    return items


def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == id), None)


def add_item(title):
    requests.post('https://api.trello.com/1/cards?key={key}&token={token}&idList={listId}&name={name}'.format(key=KEY, token=TOKEN, listId=PENDING, name=title))
    return title


def save_item(item):
    
    if item['status'] == 'Not Started':
        list_id = PENDING
    elif item['status'] == 'Completed':
        list_id = DONE
    requests.put('https://api.trello.com/1/cards/{id}?key={key}&token={token}&name={name}&idList={listId}'.format(id=item["id"], key=KEY, token=TOKEN, name=item['title'], listId=list_id))
    return item

def toggle_status(id):
    item = get_item(id)
    if item['status'] == 'Not Started':
        item['status'] = 'Completed'
    elif item['status'] == 'Completed':
        item['status'] = 'Not Started'
    save_item(item)

def delete_item(id):
    requests.delete('https://api.trello.com/1/cards/{id}?key={key}&token={token}'.format(id=id, key=KEY, token=TOKEN))   
    return