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
from cms.models.Resource import Resource
from werkzeug.exceptions import abort

bp = Blueprint("resource", __name__)
Users=current_user
@bp.route("/resource")
def show():

    return render_template("components/showResource.html")

@bp.route("/resource/edit/<int:id>", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        hascontent = Resource.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        postID = request.form['postID']
        postType = request.form['postType']
        number = request.form['number']
        photoCaption = request.form['photoCaption']
        file = request.form['file']
        filePath = request.form['filePath']
        provider = request.form['provider']
        captionUpdate = request.form['captionUpdate']
        hascontent.postID=postID
        hascontent.postType=postType
        hascontent.number=number
        hascontent.photoCaption=photoCaption
        hascontent.file=file
        hascontent.filePath=filePath
        hascontent.provider=provider
        hascontent.captionUpdate=captionUpdate
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('resource.show'))

    else:
        hascontent = Resource.query.filter_by(id=id).first()
        return render_template("components/editResourec.html",contents=hascontent)

@bp.route("/resource/delete/<int:id>", methods=("GET", "POST"))
def delete():
    resource=Resource.query.get_or_404(id)
    db.session.delete(resource)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('resource.show'))

@bp.route("/resource/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        postID = request.form['postID']
        postType = request.form['postType']
        number = request.form['number']
        photoCaption = request.form['photoCaption']        
        file = request.form['file']
        filePath = request.form['filePath']
        provider = request.form['provider']
        captionUpdate = request.form['captionUpdate']
        photo = Resource(postID, postType, number,photoCaption,file,filePath,provider,captionUpdate)
        db.session.add(photo)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('resource.show'))
    else:
        return render_template("components/createresource.html")