from flask import Flask, render_template, request, redirect, url_for

from trello_client import Trello

app = Flask(__name__)
app.config.from_object("flask_config.Config")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", items=Trello().get_items())


@app.route("/", methods=["POST"])
def add():
    title = request.form.get("title")
    Trello().add_item(title=title)
    return redirect(url_for("index"))


@app.route(
    "/items/<string:item_id>", methods=["POST"]
)  # Should be patch, but can't do without a forms library
def complete_item(item_id):
    Trello().move_to_done(item_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
