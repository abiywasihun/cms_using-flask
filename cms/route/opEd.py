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
from cms.models.opEd import OpEd
from werkzeug.exceptions import abort

bp = Blueprint("opEd", __name__)
Users=current_user
@bp.route("/opEd")
def show():
    opEd=OpEd.query.all()
    return render_template("components/showOp-Ed.html", OpEd=opEd)

@bp.route("/opEd/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = OpEd.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        hascontent.headline=headline
        hascontent.content=content
        hascontent.category=category
        hascontent.excerpt=excerpt
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('opEd.show'))

    else:
        hascontent = OpEd.query.filter_by(id=id).first()
        return render_template("components/editOpEd.html",contents=hascontent)

@bp.route("/opEd/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    opEd=OpEd.query.get_or_404(id)
    db.session.delete(opEd)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('opEd.show'))
@bp.route("/opEd/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        current_user=Users.username
        current_date = date.today() 
        opEd = OpEd(headline, content, category,excerpt,current_date,current_user)
        db.session.add(opEd)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('opEd.show'))
    else:
        return render_template("components/createopEd.html")