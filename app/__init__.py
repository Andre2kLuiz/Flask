from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'af51as561f65sa1-f65af!!65a1f6a5f2'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views import homePage
from app.models import Contato


