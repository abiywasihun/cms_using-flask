from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from cms import db
from werkzeug.exceptions import abort

bp = Blueprint("column", __name__)

@bp.route("/column")
def show():
    return render_template("components/showColumn.html")
@bp.route("/column/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        return "Hello World!"
    else:
        return render_template("components/editColumn.html")
@bp.route("/column/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        return "Hello World!"
    else:
        return render_template("components/createColumn.html")
@bp.route("/column/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    if request.method == "POST":
        return "Hello World!"
    else:
        return render_template("components/deleteColumn.html")