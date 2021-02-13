import os
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = "SuperSecretKey"
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
from cms.models.Column import Column
from cms.models.Content import Content
from cms.models.Users import User
from cms.models.Events import Events
from cms.models.AddtionalContent import AddtionalContent
from cms.models.Contact import Contact
from cms.models.EdtionBudget import EdtionBudget
from cms.models.MyTask import MyTask
from cms.models.opEd import OpEd
from cms.models.Photo import Photo
from cms.models.Resource import Resource
from cms.models.SocialMediaExcerpt import SocialMediaExcerpt
from cms.models.SocialMediaSchedule import SocialMediaSchedule
from cms.models.ThisWeekMinute import ThisWeekMinute
from cms.route import content, column, main_landing, auth, addtionalContent,contact,events,myTask,opEd,photo

from cms.route import resource, socialMediaExcerpt,socialMediaSchedule,storyProposal,thisWeekMinute,edtionBudget,websiteContent

app.register_blueprint(main_landing.bp)
app.register_blueprint(content.bp)
app.register_blueprint(column.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(addtionalContent.bp)
app.register_blueprint(contact.bp)
app.register_blueprint(edtionBudget.bp)
app.register_blueprint(events.bp)
app.register_blueprint(myTask.bp)
app.register_blueprint(opEd.bp)
app.register_blueprint(photo.bp)
app.register_blueprint(resource.bp)
app.register_blueprint(socialMediaExcerpt.bp)
app.register_blueprint(socialMediaSchedule.bp)
app.register_blueprint(storyProposal.bp)
app.register_blueprint(thisWeekMinute.bp)
app.register_blueprint(websiteContent.bp)

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    #app.config.from_mapping(
        # a default secret that should be overridden by instance config
     #   SECRET_KEY="dev",
        # store the database in the instance folder
     #   DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
   # )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
   
    #from flaskr import db

   # db.init_app(app)

    # apply the blueprints to the app
    #from cms.route import content, column, index

    #app.register_blueprint(index.bp)
    #app.register_blueprint(content.bp)
    #app.register_blueprint(column.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app