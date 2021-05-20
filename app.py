from flask import Flask, render_template, request, redirect, url_for, flash
import mongo as mongo
import view_model as view_model
import dotenv
from flask_login import login_required, login_user, current_user
import login_manager as login_manager
from oauthlib.oauth2 import WebApplicationClient
import os
import requests
import json
from user import User
from flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.config['LOGIN_DISABLED'] = os.environ.get('LOAD_DISABLED', 'False').lower() in ['true', '1']
    login_manager.login_manager.init_app(app)

    @app.route('/', methods=['Get'])
    @login_required
    def index():
        items = mongo.fetch_all_items()
        items.sort(key=lambda k: k.status, reverse=True)
        item_view_model = view_model.ViewModel(items)
        if current_user.is_active == True:
            if current_user.role == 'writer':
                return render_template('index_writer.html', view_model=item_view_model)
            elif current_user.role == 'reader':
                return render_template('index_reader.html', view_model=item_view_model)
            else:
                return render_template('index_writer.html', view_model=item_view_model)
        else:
            return render_template('index_writer.html', view_model=item_view_model)
        

    @app.route('/add', methods=['Post'])
    @login_required
    def add_todo():
        if current_user.is_active == True:
            if current_user.role == 'writer':
                mongo.create_new_item(request.form.get('title'))
                return redirect('/')
            else :
                flash('You do not have access. Please contact an admin')
                return redirect('/')
        else:
            mongo.create_new_item(request.form.get('title'))
            return redirect('/')

    @app.route('/doing_item/<todo_id>', methods=['Post'])
    @login_required
    def update_status_doing(todo_id):
        mongo.update_item_doing(todo_id)
        return redirect('/')

    @app.route('/done_item/<todo_id>', methods=['Post'])
    @login_required
    def update_status_done(todo_id):
        mongo.update_item_done(todo_id)
        return redirect('/')

    @app.route('/delete/<todo_id>', methods=['Post'])
    @login_required
    def remove_item(todo_id):
        mongo.delete_item(todo_id)
        return redirect('/')

    @app.route('/login/callback')
    def login_callback():
        callback_code = request.args.get("code")
        github_client =  WebApplicationClient(os.environ.get('clientId'))
        github_token = github_client.prepare_token_request("https://github.com/login/oauth/access_token", code=callback_code) 
        github_access = requests.post(github_token[0], headers=github_token[1], data=github_token[2], auth=(os.environ.get('clientId'), os.environ.get('client_secret_m10')))
        github_json = github_client.parse_request_body_response(github_access.text)
        github_user_request_param = github_client.add_token("https://api.github.com/user")
        github_user = requests.get(github_user_request_param[0], headers=github_user_request_param[1]).json()

        login_user(User(github_user))

        mongo.add_user_mongo(current_user)

        return redirect('/') 

    @app.route('/users', methods=['Get'])
    @login_required
    def users():
        if current_user.role == 'admin':
            users = mongo.fetch_all_users()
            return render_template('index_users.html', users=users)
        else:
            flash('You do not have access. Please contact an admin')
            return redirect('/')

    @app.route('/users/make_admin/<userid>', methods=['Post'])
    @login_required
    def make_admin(userid):
        mongo.make_admin(userid)
        return  redirect('/users')

    @app.route('/users/make_reader/<userid>', methods=['Post'])
    @login_required
    def make_reader(userid):
        mongo.make_reader(userid)
        return  redirect('/users')


    if __name__ == '__main__':
        app.run()  
    
    return app 


