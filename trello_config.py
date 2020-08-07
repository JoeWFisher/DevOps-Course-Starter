# trello API credentials
import os

BASE_URL = 'https://api.trello.com/1'

# TODO The enviroment variables are not being pulled in so this would always error 

KEY = os.environ.get('TRELLO_KEY')
#if not KEY:
#    raise ValueError("No api KEY for trello set")

TOKEN = os.environ.get('TRELLO_TOKEN')
#if not TOKEN:
#    raise ValueError("No api TOKEN for trello set")

BOARD = os.environ.get('TRELLO_BOARD')
#if not BOARD:
#    raise ValueError("No BOARD id set for trello")