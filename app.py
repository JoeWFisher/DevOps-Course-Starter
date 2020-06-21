from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import trello as trello

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['Get'])
def index():
    todos = trello.fetch_all_cards()
    todos = sorted(todos, key=lambda k: k['status'], reverse=True)
    return render_template('index.html', todos = todos)

@app.route('/add', methods=['Post'])
def add_todo():
    trello.create_new_card(request.form.get('title'))
    return redirect('/')

@app.route('/update/<int:todo_id>', methods=['Post'])
def update_status(todo_id):
    item = session.get_item(todo_id)
    item['status'] = 'Completed'
    session.save_item(item)
    return redirect('/')

@app.route('/delete/<int:todo_id>', methods=['Post'])
def remove_item(todo_id):
    item = session.get_item(todo_id)
    session.delete_item(item)
    return redirect('/')

if __name__ == '__main__':
    app.run()
