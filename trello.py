import Item as it
import requests 
import json
import os
import pymongo
import datetime

def fetch_all_items():
    item_list = []

    client = pymongo.MongoClient("mongodb+srv://devops-user:Test123@cluster0.ciffq.mongodb.net/todo_db?retryWrites=true&w=majority")
    db = client.todo_db
    ToDoCollection = db['ToDoCollection']
    for ToDo in ToDoCollection.find():
        ToDo['']

    params = (
        ('key', os.environ['Key']),
        ('token', os.environ['TOKEN']),
        ('fields', 'name,idList,dateLastActivity')
    )

    r = requests.get('https://api.trello.com/1/boards/' + os.environ['BoardID'] + '/cards', params=params)
    data = r.json()
    item_list = []
    for card in data:
        if card['idList'] == os.environ['ToDoId']:
            card['idList'] = 'To Do'
        elif card['idList'] == os.environ['DoingId']:
            card['idList'] = 'Doing'
        elif card['idList'] == os.environ['DoneId']:
            card['idList'] = 'Done'
        
        if [item for item in item_list if item.id == card['id']]:
            pass
        else:
            item_list.append(it.Item(id=card['id'], status=card['idList'], title=card['name'], last_modified=card['dateLastActivity']))
    return item_list   

def create_new_item(name):
    client = pymongo.MongoClient("mongodb+srv://devops-user:Test123@cluster0.ciffq.mongodb.net/todo_db?retryWrites=true&w=majority")
    db = client.todo_db
    todo = db.ToDoCollection
    item = {"name": name, "status": "To Do", "last_modified": datetime.datetime.now()}
    todo.insert_one(item).inserted_id

def update_item_doing(id):
        params = (
            ('key', os.environ['Key']),
            ('token', os.environ['TOKEN']),
            ('idList', os.environ['DoingId'])
        )    

        requests.put("https://api.trello.com/1/cards/" + id, params=params)
    
def update_item_done(id):    
        params = (
            ('key', os.environ['Key']),
            ('token', os.environ['TOKEN']),
            ('idList', os.environ['DoneId'])
        )    

        requests.put("https://api.trello.com/1/cards/" + id, params=params)

def delete_item(id):
    params = (
        ('key', os.environ['Key']),
        ('token', os.environ['TOKEN'])
    )    

    requests.delete("https://api.trello.com/1/cards/" + id, params=params)

def create_trello_board():
    params = (
        ('key', os.environ['Key']),
        ('token', os.environ['TOKEN']),
        ('name', 'TestDevOps')
    )    

    response = requests.post("https://api.trello.com/1/boards/", params=params)

    return response.json()['id']

def delete_trello_board(id):
    params = (
        ('key', os.environ['Key']),
        ('token', os.environ['TOKEN'])
    )    

    requests.delete("https://api.trello.com/1/boards/" + id, params=params)
