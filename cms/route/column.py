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
#from cms.models.Users import User
from werkzeug.exceptions import abort

bp = Blueprint("column", __name__)
Users=current_user
@bp.route("/column")
def show():
    column=Column.query.all()
    return render_template("components/showColumn.html",columns=column)
@bp.route("/column/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = Column.query.filter_by(id=id).first()
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
        return redirect(url_for('column.show'))
    else:
        hascontent = Column.query.filter_by(id=id).first()
        return render_template("components/editColumn.html",columns=hascontent)
@bp.route("/column/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        current_user=Users.username
        current_date = date.today() 
        column = Column(headline, content, category,excerpt,current_date,current_user)
        db.session.add(column)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('column.show'))
    else:
        return render_template("components/createColumn.html")
@bp.route("/column/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
  #  if request.method == "POST":
    column=Column.query.get_or_404(id)
    db.session.delete(column)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('column.show'))
    #else:
     #   return render_template("components/deleteColumn.html")

#retrive json response
@bp.route("/get/all/column")
def getall():
    try:
        columns=Column.query.all()
        return  jsonify([e.serialize() for e in columns])
    except Exception as e:
	    return(str(e))

@bp.route("/get/column/<id_>")
def get_by_id(id_):
    try:
        column=Column.query.filter_by(id=id_).first()
        return jsonify(column.serialize())
    except Exception as e:
	    return(str(e))