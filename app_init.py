# app_init.py
import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

basedir = pathlib.Path(__file__).parent.resolve()
app_name = __name__
app_name = 'app'
connex_app = connexion.App(app_name, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'hospital.db'}"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
mar = Marshmallow(app)
# Create the Flask-RESTful API manager.
api = Api(app)