from flask_login import LoginManager
from flask import session, redirect
from oauthlib.oauth2 import WebApplicationClient
import requests
import os
from user import User
import mongo as mongo

login_manager = LoginManager()

@login_manager.unauthorized_handler
def unauthenticated():
    github_client =  WebApplicationClient(os.environ.get('clientId'))
    github_redirect = github_client.prepare_request_uri("https://github.com/login/oauth/authorize")

    return redirect(github_redirect)  

@login_manager.user_loader
def load_user(github_user):
    
    user = mongo.fetch_user(github_user)
    user['login'] = user.pop('name')

    return User(user)
