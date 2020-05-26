from flask import Flask, render_template, request, redirect, url_for
from operator import itemgetter 
import session_items as session


app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        session.add_item(request.form.get('title'))
    return render_template('/index.html', all_items=sorted(session.get_items(), key=itemgetter('status'), reverse=True))

@app.route('/toggle-completion/<id>')
def toggle(id):
    item = session.get_item(id)
    if item['status'] == 'Not Started':
        item['status'] = 'Completed'
    elif item['status'] == 'Completed':
        item['status'] = 'Not Started'
    session.save_item(item)
    return redirect('/')

@app.route('/delete/<id>')
def delete_item(id):
    session.delete_item(id)
    return redirect('/')


if __name__ == '__main__':
    app.run()
