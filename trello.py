from config import KEY, TOKEN, BoardID
import requests 

def fetch_all_cards():
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('fields', 'name,idList')
    )

    response = requests.get('https://api.trello.com/1/boards/5eef26d3f3a754437122f88b/cards', params=params)
    cards = response.json()
    for card in cards:
        card['title'] = card.pop('name')
        card['status'] = card.pop('idList')
        if card['status'] == '5eef26d392d5ac04eb7c007c':
            card['status'] = 'Not Started'
        elif card['status'] == '5eef26d3edf8473b06a305ff':
            card['status'] = 'Complete'
    #print(cards)
    return cards
    

fetch_all_cards()