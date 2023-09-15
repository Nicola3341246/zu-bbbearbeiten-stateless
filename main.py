import helper
from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    items = helper.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("date")
    helper.add(text, date)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))


@app.route("/delete_all")
def delete_all():
    helper.delete_all()
    return redirect(url_for("index"))

@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition":"attachment; filename=zu-bbbearbeiten.csv"},
    )

