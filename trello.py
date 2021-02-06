import Item as it
import requests 
import json
import os
import pymongo
import datetime
from bson import ObjectId


def fetch_all_items():
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')
    item_list = []

    client = pymongo.MongoClient(Mongo_Url)
    db = client[Mongo_db]
    ToDoCollection = db.ToDoCollection
    for ToDo in ToDoCollection.find():
        item_list.append(it.Item(id=ToDo['_id'], status=ToDo['status'], title=ToDo['name'], last_modified=str(ToDo['last_modified'])))
    
    return item_list


def create_new_item(name):
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')

    client = pymongo.MongoClient(Mongo_Url)
    db = client[Mongo_db]
    todo = db.ToDoCollection
    item = {"name": name, "status": "To Do", "last_modified": datetime.datetime.now()}
    todo.insert_one(item).inserted_id

def update_item_doing(id):
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')

    client = pymongo.MongoClient(Mongo_Url)
    db = client[Mongo_db]
    col = db.ToDoCollection

    myquery = {"_id": ObjectId(id)}
    newvalues = {"$set": { "status": "Doing"}}

    col.update_one(myquery, newvalues)
    
def update_item_done(id): 
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')

    client = pymongo.MongoClient(Mongo_Url)
    db = client[Mongo_db]
    col = db.ToDoCollection

    myquery = {"_id": ObjectId(id)}
    newvalues = {"$set": { "status": "Done"}}

    col.update_one(myquery, newvalues)   

def delete_item(id):
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')

    client = pymongo.MongoClient(Mongo_Url)
    db = client[Mongo_db]
    col = db.ToDoCollection

    myquery = {"_id": ObjectId(id)}

    col.delete_one(myquery)  


def create_trello_board():
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')

    client = pymongo.MongoClient(Mongo_Url)
    client[Mongo_db]

    return "todo_test_db"


def delete_trello_board():
    Mongo_Url = os.environ.get('Mongo_Url')
    Mongo_db = os.environ.get('Mongo_db')

    client = pymongo.MongoClient(Mongo_Url)
    client.drop_database(Mongo_db)


