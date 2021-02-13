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
#from datetime import date
from cms.models.SocialMediaSchedule import SocialMediaSchedule
from werkzeug.exceptions import abort

bp = Blueprint("socialMediaSchedule", __name__)
Users=current_user
@bp.route("/socialMediaSchedule")
def show():

    return render_template("components/showSocialMediaSchedule.html")

@bp.route("/socialMediaSchedule/edit/<int:id>", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        hascontent = SocialMediaSchedule.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        title = request.form['title']
        time = request.form['time']
        date = request.form['date']
        permalink = request.form['permalink']
        excerpt = request.form['permalink']
        status = request.form['permalink']
        review = request.form['permalink']
        author = request.form['permalink']
        hascontent.title=title
        hascontent.time=time
        hascontent.date=date
        hascontent.permalink=permalink
        hascontent.excerpt=excerpt
        hascontent.status=status
        hascontent.review=review
        hascontent.author=author
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('socialMediaSchedule.show'))

    else:
        hascontent = SocialMediaSchedule.query.filter_by(id=id).first()
        return render_template("components/editSocialMediaSchedule.html",contents=hascontent)

@bp.route("/socialMediaSchedule/delete/<int:id>", methods=("GET", "POST"))
def delete():
    socialMediaSchedule=SocialMediaSchedule.query.get_or_404(id)
    db.session.delete(socialMediaSchedule)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('socialMediaSchedule.show'))
@bp.route("/socialMediaSchedule/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form['title']
        time = request.form['time']
        date = request.form['date']
        permalink = request.form['permalink']
        excerpt = request.form['permalink']
        status = request.form['permalink']
        review = request.form['permalink']
        author = request.form['permalink']
        socialMediaSchedule = SocialMediaSchedule(title, time, date,permalink,excerpt,status,review,author)
        db.session.add(socialMediaSchedule)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('socialMediaSchedule.show'))
    else:
        return render_template("components/createsocialMediaSchedule.html")