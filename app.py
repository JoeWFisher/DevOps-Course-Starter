from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/index')
def index():
    todos = session.get_items()
    return render_template('index.html', todos = todos)

@app.route('/index/add', methods=['Post'])
def add_todo():
    item = session.add_item(request.form.get('title'))
    session.save_item(item)
    return redirect('/index')

if __name__ == '__main__':
    app.run()
