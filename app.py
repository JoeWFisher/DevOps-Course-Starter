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

client = TrelloClient(
    api_key=os.getenv('API_KEY'),
    token=os.getenv('TOKEN')
)

board = client.get_board((os.getenv('BOARD_ID')))

@app.route('/')
def index():   
    items = []
    board_lists = board.list_lists()
    for list_item in board_lists:
        for card in list_item.list_cards():
            items.append(TrelloItem(card.id, list_item.name,card.name))
    return render_template('index.html', items = items)


@app.route('/', methods=['POST'])
def add_list():
    new_item = request.form.get('todoitem')
    board_lists = board.list_lists()
    todo_list = next((x for x in board_lists if x.name == "Things To Do"), None)
    todo_list.add_card(new_item);  
    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):

    board_lists = board.list_lists()
    todo_list = next((x for x in board_lists if x.name == "Things To Do"), None)
    done_list = next((x for x in board_lists if x.name == "Done"), None)

    cards = todo_list.list_cards()
    card = next((x for x in cards if x.id == id), None)   
    card.change_list(done_list.id)  
    return redirect(url_for('index')) 


if __name__ == '__main__':
    app.run()