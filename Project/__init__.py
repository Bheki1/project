from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)


app.config['SECRET_KEY'] = 'hamba nathi'
from Project import routes

