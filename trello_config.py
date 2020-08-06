# trello API credentials
import os

BASE_URL = 'https://api.trello.com/1'

KEY = os.environ.get('TRELLO_KEY')
TOKEN = os.environ.get('TRELLO_TOKEN')
BOARD = os.environ.get('TRELLO_BOARD')