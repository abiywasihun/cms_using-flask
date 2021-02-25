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
from cms.models.StoryProposal import StoryProposal
from werkzeug.exceptions import abort

bp = Blueprint("storyProposal", __name__)
Users=current_user
@bp.route("/storyProposal")
def show():
    storyProposal=StoryProposal.query.all()    

    return render_template("components/showStoryProposal.html",storyProposal=storyProposal)

@bp.route("/storyProposal/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = StoryProposal.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        reporter = request.form['reporter']
        number = request.form['number']
        initialHeadline = request.form['initialHeadline']
        possibleIssues = request.form['possibleIssues']
        initialLead = request.form['initialLead']
        contextOfStory = request.form['contextOfStory']
        institutionsToVisit = request.form['institutionsToVisit']
        listOfMaterial = request.form['listOfMaterial']
        listOfPeople = request.form['listOfPeople']
        listOfExpert = request.form['listOfExpert']
        nameOfExpert = request.form['nameOfExpert']
        suggestionMedia = request.form['suggestionMedia']
        section = request.form['section']
        status = request.form['status']
        updated_at = date.today() 
        hascontent.reporter=reporter
        hascontent.number=number
        hascontent.initialHeadline=initialHeadline
        hascontent.possibleIssues=possibleIssues
        hascontent.initialLead=initialLead
        hascontent.contextOfStory=contextOfStory
        hascontent.institutionsToVisit=institutionsToVisit
        hascontent.listOfMaterial=listOfMaterial
        hascontent.listOfPeople=listOfPeople
        hascontent.listOfExpert=listOfExpert
        hascontent.nameOfExpert=nameOfExpert
        hascontent.suggestionMedia=suggestionMedia
        hascontent.section=section
        hascontent.status=status
        hascontent.updated_at=updated_at
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('storyProposal.show'))

    else:
        hascontent = StoryProposal.query.filter_by(id=id).first()
        return render_template("components/editStoryProposal.html",contents=hascontent)

@bp.route("/storyProposal/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    storyProposal=StoryProposal.query.get_or_404(id)
    db.session.delete(storyProposal)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('storyProposal.show'))

@bp.route("/storyProposal/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        reporter = request.form['reporter']
        number = request.form['number']
        initialHeadline = request.form['initialHeadline']
        possibleIssues = request.form['possibleIssues']
        initialLead = request.form['initialLead']
        contextOfStory = request.form['contextOfStory']
        institutionsToVisit = request.form['institutionsToVisit']
        listOfMaterial = request.form['listOfMaterial']
        listOfPeople = request.form['listOfPeople']
        listOfExpert = request.form['listOfExpert']
        nameOfExpert = request.form['nameOfExpert']
        suggestionMedia = request.form['suggestionMedia']
        section = request.form['section']
        draftID =0
        status = request.form['status']
        updated_at = date.today() 
        storyProposal = StoryProposal(reporter, number, initialHeadline,possibleIssues,initialLead,contextOfStory,
                                institutionsToVisit,listOfMaterial,listOfPeople,listOfExpert,nameOfExpert,suggestionMedia,
                                section,draftID,status,updated_at)
        db.session.add(storyProposal)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('storyProposal.show'))
    else:
        return render_template("components/createstoryProposal.html")