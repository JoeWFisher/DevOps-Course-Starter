from config import KEY, TOKEN, BoardID
import requests 
import json

def fetch_all_cards():
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('fields', 'name,idList')
    )

    r = requests.get('https://api.trello.com/1/boards/5eef26d3f3a754437122f88b/cards', params=params)
    cards = r.json()
    for card in cards:
        card['title'] = card.pop('name')
        card['status'] = card.pop('idList')
        if card['status'] == '5eef26d392d5ac04eb7c007c':
            card['status'] = 'Not Started'
        elif card['status'] == '5eef26d3edf8473b06a305ff':
            card['status'] = 'Complete'
    return cards  

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

#update_card('5eef319da76ce3363a32156f')