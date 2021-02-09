from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from flask_login import  login_required
bp = Blueprint("main_landing", __name__)

@bp.route("/")
@login_required
def index():
    return render_template("components/main_landing.html")
    
@bp.before_request
def before_request():
    g.user = None