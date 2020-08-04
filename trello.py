from config import KEY, TOKEN, BoardID, ToDoId, DoneId, DoingId
import Item as it
import requests 
import json

def fetch_all_items():
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('fields', 'name,idList')
    )

    r = requests.get('https://api.trello.com/1/boards/' + BoardID + '/cards', params=params)
    data = r.json()
    item_list = []
    for card in data:
        if card['idList'] == ToDoId:
            card['idList'] = 'To Do'
        elif card['idList'] == DoingId:
            card['idList'] = 'Doing'
        elif card['idList'] == DoneId:
            card['idList'] = 'Done'
        
        if [item for item in item_list if item.id == card['id']]:
            pass
        else:
            item_list.append(it.Item(id=card['id'], status=card['idList'], title=card['name']))
    return item_list   

def create_new_item(name):
    params = (
        ('key', KEY),
        ('token', TOKEN),
        ('name', name),
        ('idList', ToDoId)
    )

    requests.post('https://api.trello.com/1/cards', params=params)

def update_item_doing(id):
        params = (
            ('key', KEY),
            ('token', TOKEN),
            ('idList', DoingId)
        )    

        requests.put("https://api.trello.com/1/cards/" + id, params=params)
    
def update_item_done(id):    
        params = (
            ('key', KEY),
            ('token', TOKEN),
            ('idList', DoneId)
        )    

        requests.put("https://api.trello.com/1/cards/" + id, params=params)

def delete_item(id):
    params = (
        ('key', KEY),
        ('token', TOKEN)
    )    

    requests.delete("https://api.trello.com/1/cards/" + id, params=params)

