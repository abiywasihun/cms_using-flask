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
login_manager.login_view = 'route.auth.login'
from cms.models.Column import Column
from cms.models.Content import Content
from cms.models.Users import User
from cms.route import content, column, main_landing, auth

app.register_blueprint(main_landing.bp)
app.register_blueprint(content.bp)
app.register_blueprint(column.bp)
app.register_blueprint(auth.bp)

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