from task_item import Item
import requests
import trello_config as config
from dateutil.parser import parse
import datetime
import json

def get_auth_params():
    return { 'key': config.KEY, 'token': config.TOKEN }

def build_url(endpoint):
    return config.BASE_URL + endpoint

def build_params(params = {}):
    params = get_auth_params()
    params.update(params)
    return params

def get_lists_info():
    params = build_params({ 'cards': 'open' })
    url = build_url(f'/boards/{config.BOARD}/lists')

    response = requests.get(url, params=params)
    lists = response.json()
    return lists

def get_list_info(name):
    lists = get_lists_info()
    return next((list for list in lists if list['name'] == name), None)


def get_items():
    lists = get_lists_info()
    items = []

    for card_list in lists:
        params = build_params({ 'cards': 'open' })
        list_id = card_list['id']
        url = build_url(f'/lists/{list_id}/cards')

        response = requests.get(url, params=params)
        cards = response.json()
        for card in cards:
            items.append(Item.from_trello_card(card, card_list['name']))

    return items

def get_item(id):
    items = get_items()
    return next((item for item in items if item.id == id), None)

def add_item(title, description):
    not_started_list_info = get_list_info('Not Started')
    not_started_list_id = not_started_list_info['id']
    requests.post(f'https://api.trello.com/1/cards?key={config.KEY}&token={config.TOKEN}&idList={not_started_list_id}&name={title}&desc={description}')
    return title

def set_status_not_started(id):
    item = get_item(id)
    item.set_status_not_started()
    save_item(item)
    return

def set_status_in_progress(id):
    item = get_item(id)
    item.set_status_in_progress()
    save_item(item)
    return

def set_status_completed(id):
    item = get_item(id)
    item.set_status_completed()
    save_item(item)
    return

def save_item(item):
    list_info = get_list_info(item.status)
    list_id = list_info['id']
    requests.put(
        'https://api.trello.com/1/cards/{id}?key={key}&token={token}&name={name}&idList={listId}'
        .format(id=item.id, key=config.KEY, token=config.TOKEN, name=item.title, listId=list_id)
    )
    return

def delete_item(id):
    requests.delete('https://api.trello.com/1/cards/{id}?key={key}&token={token}'.format(id=id, key=config.KEY, token=config.TOKEN))   
    return

