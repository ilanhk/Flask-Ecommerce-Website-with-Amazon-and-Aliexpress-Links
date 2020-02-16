from flask import Flask
from flask_sqlalchemy import SQLAlchemy #the link to python to database
from flask_migrate import Migrate #to allow migration
import random


import os  #the main purpose of the OS module is to interact with your operating system. so like a command line

# if click example flask then click 'ctrl' + 'b' you will get all the documentation of flask or whatever import you click on
# every big project should have its own database

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(16)   #need a secret key for forms
app.config['DEBUG'] = True
os.system('export FLASK_APP=run.py') #to run this is terminal


# Database Connection
db_info = {'host': 'localhost',   #localhost:5000 can be used instead 0f something like this 127.0.0.1:5000
           'database': 'hackathon2',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes, forms
