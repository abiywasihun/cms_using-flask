import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import jsonify
from flask_bcrypt import Bcrypt
from flask_login import logout_user, login_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from cms import db,app,login_manager
from cms.models.Users import User
bp = Blueprint("auth", __name__)



#login_manager.login_view = 'login'
bcrypt = Bcrypt(app)


@bp.route("/login",methods=("GET", "POST"))
def login():
    session.clear()
    if request.method == 'GET':
         return render_template("auth/signIn.html")
    
    username = request.form['username']
    password = request.form['password']

        
        
        # query the user
    registered_user = User.query.filter_by(username=username).first()

        # check the passwords
    if registered_user is None:

        flash('Invalid Username')
        return render_template('auth/signIn.html')

        
    else:
        if bcrypt.check_password_hash(registered_user.password, password) == False:
            flash('Invalid Username/Password')
            return render_template('auth/signIn.html')
            
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True

        # login the user
    login_user(registered_user, remember=remember_me)
    g.user=registered_user
    return redirect(url_for('main_landing.index'))

       
   # else:
    #    

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user):
    return User.query.get(user)
    
@bp.route("/signUp", methods=("GET","POST"))
def signup():
    if request.method == "POST":
        
        password = request.form['password']
        conf_password = request.form['confirm-password']
        username = request.form['username']
        email = request.form['email']
        if conf_password != password:
            flash("Passwords do not match")
            return render_template("auth/signUp.html")

        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # create a user, and check if its unique
        user = User(username, pw_hash, email)
        u_unique = user.unique()

        # add the user
        if u_unique == 0:
            db.session.add(user)
            db.session.commit()
            flash("Account Created")
            return redirect(url_for('auth.login'))
         # else error check what the problem is
        elif u_unique == -1:
            flash("Email address already in use.")
            return render_template("auth/signUp.html")
        elif u_unique == -2:
            flash("Username already in use.")
            return render_template("auth/signUp.html")

        else:
            flash("Username and Email already in use.")
            return render_template("auth/signUp.html")

        
    
    else:
        return render_template("auth/signUp.html")


#retrive json response
@bp.route("/get/all/user")
def getall():
    try:
        users=User.query.all()
        return  jsonify([e.serialize() for e in users])
    except Exception as e:
	    return(str(e))

@bp.route("/get/user/<id_>")
def get_by_id(id_):
    try:
        user=User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
	    return(str(e))