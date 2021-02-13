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
from cms.models.WebsiteContent import WebsiteContent
from werkzeug.exceptions import abort

bp = Blueprint("websiteContent", __name__)
Users=current_user
@bp.route("/websiteContent")
def show():

    return render_template("components/showWebsiteContent.html")

@bp.route("/websiteContent/edit/<int:id>", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        hascontent = WebsiteContent.query.filter_by(id=id).first()
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
        return redirect(url_for('websiteContent.show'))

    else:
        hascontent = WebsiteContent.query.filter_by(id=id).first()
        return render_template("components/editWebsiteContent.html",contents=hascontent)

   

@bp.route("/websiteContent/delete/<int:id>", methods=("GET", "POST"))
def delete():
    websiteContent=WebsiteContent.query.get_or_404(id)
    db.session.delete(websiteContent)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('websiteContent.show'))

@bp.route("/websiteContent/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        headline = request.form['headline']
        content = request.form['content']
        category = request.form['category']
        excerpt = request.form['excerpt']
        current_user=Users.username
        current_date = date.today() 
        websiteContent = WebsiteContent(headline, content, category,excerpt,current_date,current_user)
        db.session.add(websiteContent)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('websiteContent.show'))
    else:
        return render_template("components/createwebsiteContent.html")