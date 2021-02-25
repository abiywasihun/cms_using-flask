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
from cms.models.Events import Events
from werkzeug.exceptions import abort

bp = Blueprint("events", __name__)
Users=current_user
@bp.route("/events")
def show():
    events=Events.query.all()

    return render_template("components/showEvents.html",events=events)

@bp.route("/events/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = Events.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
         
        title = request.form['title']
        venue = request.form['venue']
        date_from_date = request.form['date_from_date']
        date_from_time = request.form['date_from_time']
        date_to_date = request.form['date_to_date']
        date_to_time = request.form['date_to_time']
        contactFirstName = request.form['contactFirstName']
        contactLastName = request.form['contactLastName']
        contactOfficeTel = request.form['contactOfficeTel']
        contactMobileNum = request.form['contactMobileNum']
        contactEmail = request.form['contactEmail']
        description = request.form['description']
        hascontent.title=title
        hascontent.venue=venue
        hascontent.date_from_date=date_from_date
        hascontent.date_from_time=date_from_time
        hascontent.date_to_date=date_to_date
        hascontent.date_to_time=date_to_time
        hascontent.contactFirstName=contactFirstName
        hascontent.contactLastName=contactLastName
        hascontent.contactOfficeTel=contactOfficeTel
        hascontent.contactMobileNum=contactMobileNum
        hascontent.contactEmail=contactEmail
        hascontent.description=description
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('events.show'))

    else:
        hascontent = Events.query.filter_by(id=id).first()
        return render_template("components/editEvent.html",contents=hascontent)

@bp.route("/events/delete/<int:id>", methods=("GET", "POST"))
def delete(id):

    event=Events.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('events.show'))

@bp.route("/events/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form['title']
        venue = request.form['venue']
        date_from_date = request.form['date_from_date']
        date_from_time = request.form['date_from_time']
        date_to_date = request.form['date_to_date']
        date_to_time = request.form['date_to_time']
        contactFirstName = request.form['contactFirstName']
        contactLastName = request.form['contactLastName']
        contactOfficeTel = request.form['contactOfficeTel']
        contactMobileNum = request.form['contactMobileNum']
        contactEmail = request.form['contactEmail']
        description = request.form['description']
        createdBy=Users.username
        created_at = date.today() 
        events = Events(title, venue, date_from_date,date_from_time,date_to_date,date_to_time,contactFirstName,contactLastName,
                         contactOfficeTel,contactMobileNum,contactEmail,description,createdBy,created_at)
        db.session.add(events)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('events.show'))
    else:
        return render_template("components/createvents.html")