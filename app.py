from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():

    return render_template('index.html', list=session.get_items())

@app.route('/delete/<int:id>')
def delete_task(id):
    session.remove_item(id)
    return render_template('index.html', list=session.get_items())

@app.route('/complete/<int:id>')
def complete_task(id):
    update = session.get_item(id)
    update['status']='Complete'
    session.save_item(update)
    return render_template('index.html', list=session.get_items())

@app.route('/', methods=['POST'])
def add_list():
 # Code to create a new book entry in the database.
    todo = request.form.get('todoitem')
    session.add_item(todo)
    return render_template('index.html', list=session.get_items())

if __name__ == '__main__':
    app.run()