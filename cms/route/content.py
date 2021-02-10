from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from cms.models.Content import Content
from cms.models.Users import User
from cms import db
from datetime import date
from flask_login import current_user
from werkzeug.exceptions import abort

bp = Blueprint("content", __name__)
Users=current_user
@bp.route("/content")
def show():
    content=Content.query.all()
    return render_template("components/showContent.html",contents=content)
   # return render_template("components/showContent.html")
@bp.route("/content/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        contenthas = Content.query.filter_by(id=id).first()
        if contenthas is None:
            return redirect(url_for('content.show'))
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        contenthas.headline=headline
        contenthas.content=content
        contenthas.category=category
        contenthas.excerpt=excerpt
        db.session.add(contenthas)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('content.show'))

    else:
        contenthas = Content.query.filter_by(id=id).first()
        return render_template("components/editContent.html",contents=contenthas)
@bp.route("/content/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        current_user=Users.username
        current_date = date.today() 
        column = Content(headline, content, category,excerpt,current_date,current_user)
        db.session.add(column)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('content.show'))
    else:
        return render_template("components/creatContent.html")
@bp.route("/content/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    if request.method == "POST":
        content=Content.query.get_or_404(id)
        db.session.delete(content)
        db.session.commit()
        flash("Content Deleted Succesfully")
        return redirect(url_for('content.show'))
    else:
        return render_template("components/deleteContent.html")

#retrive json response
@bp.route("/get/all/content")
def getall():
    try:
        contents=Content.query.all()
        return  jsonify([e.serialize() for e in contents])
    except Exception as e:
	    return(str(e))

@bp.route("/get/content/<id_>")
def get_by_id(id_):
    try:
        content=Content.query.filter_by(id=id_).first()
        return jsonify(content.serialize())
    except Exception as e:
	    return(str(e))