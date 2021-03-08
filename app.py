from flask import Flask, render_template, request, redirect, url_for
import trello as trello
import view_model as view_model
import dotenv
from flask_login import login_required
import login_manager as login_manager
from oauthlib.oauth2 import WebApplicationClient
import os
import requests
import json

def create_app():
    app = Flask(__name__)
    app.config.from_object(dotenv.load_dotenv(dotenv.find_dotenv('.env')))
    login_manager.login_manager.init_app(app)

    @app.route('/', methods=['Get'])
    def index():
        items = trello.fetch_all_items()
        items.sort(key=lambda k: k.status, reverse=True)
        item_view_model = view_model.ViewModel(items)
        return render_template('index.html', view_model=item_view_model) 

    @app.route('/add', methods=['Post'])
    @login_required
    def add_todo():
        trello.create_new_item(request.form.get('title'))
        return redirect('/')

    @app.route('/doing_item/<todo_id>', methods=['Post'])
    def update_status_doing(todo_id):
        trello.update_item_doing(todo_id)
        return redirect('/')

    @app.route('/done_item/<todo_id>', methods=['Post'])
    def update_status_done(todo_id):
        trello.update_item_done(todo_id)
        return redirect('/')

    @app.route('/delete/<todo_id>', methods=['Post'])
    def remove_item(todo_id):
        trello.delete_item(todo_id)
        return redirect('/')

    @app.route('/login/callback')
    def login_callback():
        callback_code = request.args.get("code")
        github_client =  WebApplicationClient(os.environ.get('clientId'))
        github_token = github_client.prepare_token_request("https://github.com/login/oauth/access_token", code=callback_code) 
        github_user = github_client.add_token("https://api.github.com/user", Authorization=github_token)

        return redirect('/') 
    if __name__ == '__main__':
        app.run()  
    
    return app 


