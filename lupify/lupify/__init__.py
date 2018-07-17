from os import path, getcwd

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from pymongo import MongoClient
from configparser import ConfigParser

basedir = path.abspath(path.dirname(__file__))

__location__ = path.realpath(
    path.join(getcwd(), path.dirname(__file__))
)
config = ConfigParser()
config.read(path.join(__location__, 'config.ini'))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
app.config['WTF_CSRF_SECRET_KEY'] = '8702d997ad5988fbf2d6b950aa1167528191a356573a92847b9cdc533a511e03'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'lupify.db')
#db = SQLAlchemy(app)

# mongoClient = MongoClient('127.0.0.1', 27017)

try:
    mongodb_uri = config.get("config", "mongodb_uri")
    mongodb_user = config.get("config", "mongodb_user")
    mongodb_pass = config.get("config", "mongodb_pass")

    mongoClient = MongoClient(mongodb_uri, 27017)
    db = mongoClient.lupify
    db.authenticate(mongodb_user, mongodb_pass)
except:
    print("Failed to connect to MongoDB")

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)

import lupify.models
import lupify.views