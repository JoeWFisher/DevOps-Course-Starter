from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/index', methods=['Get', 'Put'])
def index():
    todos = session.get_items()
    return render_template('index.html', todos = todos)

@app.route('/index/add', methods=['Post'])
def add_todo():
    session.add_item(request.form.get('title'))
    return redirect('/index')

@app.route('/index/update/<int:todo_id>', methods=['Get','Put'])
def update_status(todo_id):
    item = session.get_item(todo_id)
    item['status'] = 'Completed'
    session.save_item(item)
    return redirect('/index')

@app.route('/index/delete/<int:todo_id>', methods=['Get', 'Delete'])
def remove_item(todo_id):
    item = session.get_item(todo_id)
    session.delete_item(item)
    return redirect('/index')

if __name__ == '__main__':
    app.run()
