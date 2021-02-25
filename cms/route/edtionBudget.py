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
from cms.models.EdtionBudget import EdtionBudget
from werkzeug.exceptions import abort

bp = Blueprint("edtionBudget", __name__)
Users=current_user
@bp.route("/edtionBudget")
def show():
    edtionBudget=EdtionBudget.query.all()
    return render_template("components/showEdtionBudget.html",edtionBudget=edtionBudget)

@bp.route("/edtionBudget/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        hascontent = EdtionBudget.query.filter_by(id=id).first()
        if hascontent is None:
            return redirect(url_for('content.show'))
        total_page = request.form['total_page']
        number = request.form['number']
        volume = request.form['volume']
        total_advertisement = request.form['total_advertisement']
        no_of_color_pages = request.form['no_of_color_pages']
        hascontent.total_page=total_page
        hascontent.number=number
        hascontent.volume=volume
        hascontent.total_advertisement=total_advertisement
        hascontent.no_of_color_pages=no_of_color_pages
        db.session.add(hascontent)
        db.session.commit()
        flash("Content Updated Succesfully")
        return redirect(url_for('edtionBudget.show'))

    else:
        hascontent = EdtionBudget.query.filter_by(id=id).first()
        return render_template("components/editEdtionBuget.html",contents=hascontent)

@bp.route("/edtionBudget/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    edtionbudeget=EdtionBudget.query.get_or_404(id)
    db.session.delete(edtionbudeget)
    db.session.commit()
    flash("Content Deleted Succesfully")
    return redirect(url_for('edtionBudget.show'))

@bp.route("/edtionBudget/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        total_page = request.form['total_page']
        number = request.form['number']
        volume = request.form['volume']
        total_advertisement = request.form['total_advertisement']
        no_of_color_pages = request.form['no_of_color_pages']
        created_by=Users.username
        created_at = date.today() 
        edtionBudget = EdtionBudget(total_page, number, volume,total_advertisement,no_of_color_pages,created_at,created_by)
        db.session.add(edtionBudget)
        db.session.commit()
        flash("Content Created Succesfully")
        return redirect(url_for('edtionBudget.show'))
    else:
        return render_template("components/createdtionBudget.html")