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
    websiteContent=WebsiteContent.query.all()

    return render_template("components/showWebsiteContent.html", websiteContent=websiteContent)

@bp.route("/websiteContent/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = WebsiteContent.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        category = request.form['category']
        headline = request.form['headline']
        sub_headline = request.form['sub_headline']
        article = request.form['article']
        nutshell = request.form['nutshell']
        blurb = request.form['blurb']
        pullout = request.form['pullout']
        author = request.form['author']
        author_description = request.form['author_description']
        number = request.form['number']
        volume = request.form['volume']
        status = request.form['status']
        hascontent.category=category
        hascontent.headline=headline
        hascontent.sub_headline=sub_headline
        hascontent.article=article
        hascontent.nutshell=nutshell
        hascontent.blurb=blurb
        hascontent.pullout=pullout
        hascontent.author=author
        hascontent.author_description=author_description
        hascontent.number=number
        hascontent.volume=volume
        hascontent.status=status
        db.session.add(hascontent)
        db.session.commit()
        return redirect(url_for('websiteContent.show'))

    else:
        hascontent = WebsiteContent.query.filter_by(id=id).first()
        return render_template("components/editWebsiteContent.html",contents=hascontent)

   

@bp.route("/websiteContent/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    websiteContent=WebsiteContent.query.get_or_404(id)
    db.session.delete(websiteContent)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('websiteContent.show'))

@bp.route("/websiteContent/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        category = request.form['category']
        headline = request.form['headline']
        sub_headline = request.form['sub_headline']
        article = request.form['article']
        nutshell = request.form['nutshell']
        blurb = request.form['blurb']
        pullout = request.form['pullout']
        author = request.form['author']
        author_description = request.form['author_description']
        number = request.form['number']
        volume = request.form['volume']
        status = request.form['status']
        created_by =Users.username
        created_date = date.today() 
        websiteContent = WebsiteContent(category, headline, sub_headline,article,nutshell,blurb,pullout,author,author_description,number,volume,status,created_by,created_date)
        db.session.add(websiteContent)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('websiteContent.show'))
    else:
        return render_template("components/createwebsiteContent.html")