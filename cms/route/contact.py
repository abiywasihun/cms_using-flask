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
from cms.models.Contact import Contact
from werkzeug.exceptions import abort

bp = Blueprint("contact", __name__)
Users=current_user
@bp.route("/contact")
def show():

    return render_template("components/showContact.html")

@bp.route("/contact/edit/<int:id>", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        hascontent = Contact.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        organization = request.form['organization']
        title = request.form['title']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        cellPhone = request.form['cellPhone']
        workPhone = request.form['workPhone']
        email = request.form['email']
        description = request.form['description']
        remark = request.form['remark']
        hascontent.organization=organization
        hascontent.title=title
        hascontent.firstName=firstName
        hascontent.lastName=lastName
        hascontent.cellPhone=cellPhone
        hascontent.workPhone=workPhone
        hascontent.email=email
        hascontent.description=description
        hascontent.remark=remark
        db.session.add(hascontent)
        db.session.commit()
        flash("Contact Updated Succesfully")
        return redirect(url_for('contact.show'))
    else:
        hascontent = Contact.query.filter_by(id=id).first()
        return render_template("components/editContact.html",columns=hascontent)

@bp.route("/contact/delete/<int:id>", methods=("GET", "POST"))
def delete():
    contact=Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact Deleted Succesfully")
    return redirect(url_for('contact.show'))

   # return "delete"

@bp.route("/contact/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        organization = request.form['organization']
        title = request.form['title']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        cellPhone = request.form['cellPhone']
        workPhone = request.form['workPhone']
        email = request.form['email']
        description = request.form['description']
        remark = request.form['remark']
        created_at = date.today() 
        contact = Contact(organization, title, firstName,lastName,cellPhone,workPhone,email,description,remark,created_at)
        db.session.add(contact)
        db.session.commit()
        flash("Contact Created Succesfully")
        return redirect(url_for('contact.show'))
    else:
        return render_template("components/createcontact.html")