from flask import Flask, render_template, request, redirect, url_for
import trello as trello
import view_model as view_model

def create_app():
    app = Flask(__name__)
    app.config.from_object('env')

    @app.route('/', methods=['Get'])
    def index():
        items = trello.fetch_all_items()
        items.sort(key=lambda k: k.status, reverse=True)
        item_view_model = view_model.ViewModel(items)
        return render_template('index.html', view_model=item_view_model) 

    @app.route('/add', methods=['Post'])
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

    if __name__ == '__main__':
        app.run()  
    
    return app 


