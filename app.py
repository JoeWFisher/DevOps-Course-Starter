from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from item import TrelloItem
from trello import TrelloClient
import session_items as session
import os
import requests
import json

app = Flask(__name__)
app.config.from_object('flask_config.Config')

load_dotenv()

TRELLO_API_KEY=os.getenv('API_KEY')
TRELLO_TOKEN=os.getenv('TOKEN')
TRELLO_BOARD_ID = '5efed139761c8e2d109e29f6'
TRELLO_TO_DO_LIST_ID = '5efed13a29959777eedf76c5'

client = TrelloClient(
    api_key=os.getenv('API_KEY'),
    token=os.getenv('TOKEN')
)
  
url = f"https://api.trello.com/1/lists/{TRELLO_TO_DO_LIST_ID}/cards"
headers = {"Accept": "application/json"}
querystring = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}


def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

def delete_card(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
    #querystring = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    response = requests.delete("DELETE",url)
    #card_id = response.json()["id"]
   # return card_id


list_of_cards = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(list_of_cards.text)

board = client.get_board((os.getenv('BOARD_ID')))

@app.route('/')
def index():   
    items = []
    board_lists = board.list_lists()
    for list_item in board_lists:
        for card in list_item.list_cards():
            #test = TrelloItem(card.id, list_item.name,card.name)
            items.append(TrelloItem(card.id, list_item.name,card.name))

    return render_template('index.html', items = items)

   # all_boards = client.list_boards()
   # last_board = all_boards[-1]
  #  last_board.list_lists()
  #  my_list = last_board.get_list(TRELLO_TO_DO_LIST_ID)

 #   for card in my_list.list_cards():
 #       print(card.name)

 #   items = []
 #   for card in data:
  #      item = {'id': card['id'], 'name': card['name']}
  #      items.append(item)
       # print(card['name'])
        
    #return render_template('index.html', items = items)

@app.route('/delete/<int:id>')
def delete_task(id):
   
    delete_card(id)
    #return redirect(url_for('index'))
    #return render_template('index.html', list=session.get_items())

@app.route('/complete/<int:id>')
def complete_task(id):
    update = session.get_item(id)
    update['status']='Complete'
    session.save_item(update)
    return render_template('index.html', list=session.get_items())

@app.route('/items/<id>/complete')
def complete_item(id):

    board_lists = board.list_lists()
    todo_list = next((x for x in board_lists if x.name == "ToDo"), None)
    done_list = next((x for x in board_lists if x.name == "Done"), None)

    cards = todo_list.list_cards()
    card = next((x for x in cards if x.id == id), None)   
    card.change_list(done_list.id)  
    return redirect(url_for('index')) 

@app.route('/items/<id>/uncomplete')
def uncomplete_item(id):
    board_lists = board.list_lists()
    todo_list = next((x for x in board_lists if x.name == "ToDo"), None)
    done_list = next((x for x in board_lists if x.name == "Done"), None)

    cards = done_list.list_cards()
    card = next((x for x in cards if x.id == id), None)   
    card.change_list(todo_list.id)  
    return redirect(url_for('index')) 


@app.route('/', methods=['POST'])
def add_list():
 # Code to create a new book entry in the database.
    todo = request.form.get('todoitem')
    create_card(TRELLO_TO_DO_LIST_ID,todo)
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()