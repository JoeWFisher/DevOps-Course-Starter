from flask import Flask, render_template, request, redirect, url_for
from operator import itemgetter 
import trello_items as trello
import view_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        trello.add_item(request.form.get('title'), request.form.get('description'))
    return render_template('/index.html', all_items=trello.get_items(), show_archive=False)

@app.route('/archive', methods=['GET'])
def archive(): 
    return render_template('/index.html', all_items=trello.get_all_items(), show_archive=True)

@app.route('/set-status/<id>/<status>')
def set_status(id, status):
    if status == 'outstanding':
        trello.set_status_not_started(id)
    elif status == 'pending':
        trello.set_status_in_progress(id)
    elif status == 'completed':
        trello.set_status_completed(id)
    return redirect('/')

@app.route('/delete/<id>')
def delete_item(id):
    trello.delete_item(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
