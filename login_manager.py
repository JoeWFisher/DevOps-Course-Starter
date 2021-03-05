from flask_login import LoginManager
from flask import session, redirect
import app
from requests_oauthlib import OAuth2Session
import requests
import os

login_manager = LoginManager()

@login_manager.unauthorized_handler
def unauthenticated():
    github = OAuth2Session(os.environ.get('clientId'))
    authorization_url, state = github.authorization_url('https://github.com/login/oauth/authorize')

    session['oauth_state'] = state
    return redirect(authorisation_url)  

@login_manager.user_loader
def load_user(user_id):
    return None

login_manager.init_app(app)