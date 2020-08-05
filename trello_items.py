import requests
from trello_config import KEY, TOKEN, BOARD, OUTSTANDING, PENDING, DONE
from dateutil.parser import parse
import datetime
import json

class Item:
    def __init__(self, card):
        self.id = card['id']
        self.title = card['name']
        self.editDatetime = parse(card['dateLastActivity'])
        if card['idList'] == OUTSTANDING:
            self.status = 'Not Started'
        elif card['idList'] == PENDING:
            self.status = 'In Progress'                
        elif card['idList'] == DONE:
            self.status = 'Completed'
        if card['desc'] != 'None':
            self.description = card['desc']

def get_all_items():
    response = requests.get(
        f'https://api.trello.com/1/boards/{BOARD}/cards',
        params={'key':KEY, 'token':TOKEN},
    )
    all_items = [Item(item) for item in response.json()]
    all_items.sort(reverse=True, key=get_status)
    return all_items

def get_status(e):
    return e.status

def get_item(id):
    items = get_all_items()
    return next((item for item in items if item.id == id), None)

def add_item(title, description):
    now = datetime.datetime.now()
    requests.post(f'https://api.trello.com/1/cards?key={KEY}&token={TOKEN}&idList={OUTSTANDING}&name={title}&desc={description}&due={now}')
    return title

def set_status_not_started(id):
    item = get_item(id)
    item.status = 'Not Started'
    save_item(item)
    return

def set_status_in_progress(id):
    item = get_item(id)
    item.status = 'In Progress'
    save_item(item)
    return

def set_status_completed(id):
    item = get_item(id)
    item.status = 'Completed'
    save_item(item)
    return

def save_item(item):
    if item.status == 'Not Started':
        list_id = OUTSTANDING
    elif item.status == 'In Progress':
        list_id = PENDING
    else:
        list_id = DONE
    requests.put(
        'https://api.trello.com/1/cards/{id}?key={key}&token={token}&name={name}&idList={listId}'
        .format(id=item.id, key=KEY, token=TOKEN, name=item.title, listId=list_id)
    )
    return

def delete_item(id):
    requests.delete('https://api.trello.com/1/cards/{id}?key={key}&token={token}'.format(id=id, key=KEY, token=TOKEN))   
    return