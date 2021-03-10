from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    email = db.Column(db.String(120), primary_key = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    timestamp = db.Column(db.DateTime, nullable = False)
    
    def __init__(self, email, password, timestamp) :
        self.email = email
        self.password = password
        self.timestamp = timestamp

    # def __repr__(self):
    #     return self.email

class participant1(db.Model):
    __tablename__ = "particpant1"
    name= db.Column(db.String(80), primary_key = True, nullable = False)
    score = db.Column(db.Integer, nullable = False)  
    def __init__(self, name,score) :
        self.name=name
        self.score=score
        

    # def __repr__(self):
    #     return self.name
