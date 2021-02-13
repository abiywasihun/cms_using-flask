from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify
from cms import db
from flask import session
from flask_login import current_user
from datetime import date
from cms.models.Column import Column
from cms.models.Users import User
from werkzeug.exceptions import abort

bp = Blueprint("storyProposal", __name__)
Users=current_user
@bp.route("/storyProposal")
def show():

    return render_template("components/showStoryProposal.html")

@bp.route("/storyProposal/edit/<int:id>", methods=("GET", "POST"))
def edit():

    return "edit"

@bp.route("/storyProposal/delete/<int:id>", methods=("GET", "POST"))
def delete():

    return "delete"

@bp.route("/storyProposal/create", methods=("GET", "POST"))
def create():
    
    return "create"