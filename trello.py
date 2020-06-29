from config import KEY, TOKEN, BoardID, TTD, DO
import requests 
import json

class Item:
    def __init__(self, id, status, title):
        self.id = id
        self.title = title
        self.status = status


def fetch_all_items():
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('fields', 'name,idList')
    )

    r = requests.get('https://api.trello.com/1/boards/5eef26d3f3a754437122f88b/cards', params=params)
    data = r.json()
    item_list = []
    for card in data:
        if card['idList'] == TTD:
            card['idList'] = 'Not Started'
        elif card['idList'] == DO:
            card['idList'] = 'Complete'

        if [item for item in item_list if item.id == card['id']]:
            pass
        else:
            item_list.append(Item(id=card['id'], status=card['idList'], title=card['name']))
    return item_list   

def create_new_item(name):
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('name', name),
        ('idList', TTD)
    )

    requests.post('https://api.trello.com/1/cards', params=params)

def update_item(id):
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('idList', DO)
    )    

    requests.put("https://api.trello.com/1/cards/" + id, params=params)

def delete_item(id):
    params = (
        ('key', KEY),
        ('token', TOKEN)
    )    

    requests.delete("https://api.trello.com/1/cards/" + id, params=params)

