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
    thisWeekMinute=ThisWeekMinute.query.all()

    return render_template("components/showThisWeekMinute.html", thisWeekMinute=thisWeekMinute)

@bp.route("/thisWeekMinute/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = ThisWeekMinute.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        category = request.form['category']
        content = request.form['content']
        number = request.form['number']
        volume = request.form['volume']
        author = request.form['author']
        section = request.form['section']
        status = request.form['status']
        headline = request.form['headline']
        updated_at = date.today() 
        hascontent.headline=headline
        hascontent.content=content
        hascontent.category=category
        hascontent.number=number
        hascontent.volume=volume
        hascontent.author=author
        hascontent.section=section
        hascontent.status=status
        hascontent.updated_at=updated_at
        
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('thisWeekMinute.show'))

    else:
        hascontent = ThisWeekMinute.query.filter_by(id=id).first()
        return render_template("components/editThisWeekMinute.html",contents=hascontent)

@bp.route("/thisWeekMinute/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    thisWeekMinute=ThisWeekMinute.query.get_or_404(id)
    db.session.delete(thisWeekMinute)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('thisWeekMinute.show'))

@bp.route("/thisWeekMinute/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        category = request.form['category']
        content = request.form['content']
        number = request.form['number']
        volume = request.form['volume']
        author = request.form['author']
        date = date.today() 
        draftID = 0
        section = request.form['section']
        status = request.form['status']
        headline = request.form['headline']
        updated_at = date.today() 
        thisWeekMinute = ThisWeekMinute(category, content, number,volume,author,draftID,section,status,headline,updated_at)
        db.session.add(thisWeekMinute)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('thisWeekMinute.show'))
    else:
        return render_template("components/createthisWeekMinute.html")