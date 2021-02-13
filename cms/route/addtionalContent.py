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
from cms.models.AddtionalContent import AddtionalContent
from werkzeug.exceptions import abort

bp = Blueprint("addtionalContent", __name__)
Users=current_user
@bp.route("/addtionalContent")
def show():

    return render_template("components/showAddtionalContent.html")

@bp.route("/addtionalContent/edit/<int:id>", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        hascontent = AddtionalContent.query.filter_by(id=id).first()
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
        return redirect(url_for('addtionalContent.show'))

    else:
        hascontent = AddtionalContent.query.filter_by(id=id).first()
        return render_template("components/editaddtionalContent.html",contents=hascontent)

@bp.route("/addtionalContent/delete/<int:id>", methods=("GET", "POST"))
def delete():
    addtionalContent=AddtionalContent.query.get_or_404(id)
    db.session.delete(addtionalContent)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('addtionalContent.show'))
@bp.route("/addtionalContent/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        current_user=Users.username
        current_date = date.today() 
        addtionalContent = AddtionalContent(headline, content, category,excerpt,current_date,current_user)
        db.session.add(addtionalContent)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('addtionalContent.show'))
    else:
        return render_template("components/createaddtionalContent.html")