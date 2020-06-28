from config import KEY, TOKEN, BoardID
import requests 
import json

class Item:
    def __init__(self, id, status, title):
        self.id = id
        self.title = title
        self.status = status

item_list = []

def fetch_all_cards():
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('fields', 'name,idList')
    )

    r = requests.get('https://api.trello.com/1/boards/5eef26d3f3a754437122f88b/cards', params=params)
    data = r.json()
    for card in data:
        if card['idList'] == '5eef26d392d5ac04eb7c007c':
            card['idList'] = 'Not Started'
        elif card['idList'] == '5eef26d3edf8473b06a305ff':
            card['idList'] = 'Complete'
        card['title'] = card.pop('name')
        card['status'] = card.pop('idList')

    item_list = data
        # if [item for item in item_list if item.id == card['id']]:
        #     pass
        # else:
        #     item_list.append(Item(id=card['id'], status=card['idList'], title=card['name']))
    return item_list

def create_new_card(name):
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('name', name),
        ('idList', '5eef26d392d5ac04eb7c007c')
    )

    requests.post('https://api.trello.com/1/cards', params=params)

def update_card(id):
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('idList', '5eef26d3edf8473b06a305ff')
    )    

    requests.put("https://api.trello.com/1/cards/" + id, params=params)

def delete_card(id):
    params = (
        ('key', KEY),
        ('token', TOKEN)
    )    

    r = requests.delete("https://api.trello.com/1/cards/" + id, params=params)

