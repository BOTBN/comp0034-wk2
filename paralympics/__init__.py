import os 

from flask import Flask 

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    # configure the Flask app (see later notes on how to generate your own SECRET_KEY)
    app.config.from_mapping(
        SECRET_KEY='Up13sOKglLaE9SeNzALS198GldtXwl18hqU',
        # Set the location of the database file called paralympics.sqlite which will be in the app's instance folder
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instance_path, 'paralympics.sqlite'),  
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

# Put the following code inside the create_app function after the code to ensure the instance folder exists
# This lis likely to be circa line 40.
    with app.app_context():
    # Register the routes with the app in the context
        from paralympics import paralympics

    return app

 
