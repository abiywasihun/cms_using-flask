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
from cms.models.ThisWeekMinute import ThisWeekMinute
from werkzeug.exceptions import abort

bp = Blueprint("thisWeekMinute", __name__)
Users=current_user
@bp.route("/thisWeekMinute")
def show():

    return render_template("components/showThisWeekMinute.html")

@bp.route("/thisWeekMinute/edit/<int:id>", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        hascontent = ThisWeekMinute.query.filter_by(id=id).first()
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
        return redirect(url_for('thisWeekMinute.show'))

    else:
        hascontent = ThisWeekMinute.query.filter_by(id=id).first()
        return render_template("components/editThisWeekMinute.html",contents=hascontent)

@bp.route("/thisWeekMinute/delete/<int:id>", methods=("GET", "POST"))
def delete():
    thisWeekMinute=ThisWeekMinute.query.get_or_404(id)
    db.session.delete(thisWeekMinute)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('thisWeekMinute.show'))

@bp.route("/thisWeekMinute/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        current_user=Users.username
        current_date = date.today() 
        thisWeekMinute = ThisWeekMinute(headline, content, category,excerpt,current_date,current_user)
        db.session.add(thisWeekMinute)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('thisWeekMinute.show'))
    else:
        return render_template("components/createthisWeekMinute.html")