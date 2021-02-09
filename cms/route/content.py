from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

bp = Blueprint("content", __name__)

@bp.route("/content")
def show():
    return render_template("components/showContent.html")
@bp.route("/content/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        return "Hello World!"
    else:
        return render_template("components/editContent.html")
@bp.route("/content/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        return "Hello World!"
    else:
        return render_template("components/createContent.html")
@bp.route("/content/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    if request.method == "POST":
        return "Hello World!"
    else:
        return render_template("components/deleteContent.html")