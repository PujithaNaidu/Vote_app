import os

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://jizezwuvqqqggm:2d53be5d779c2ce5ee025fb9a173a13d17c5c63341dd8976c1a363d52732b2d9@ec2-54-159-175-113.compute-1.amazonaws.com:5432/dd5q43uk9mpsk0'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()

