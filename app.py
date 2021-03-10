import os
from flask import Flask, session, render_template, redirect, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from create import app
import datetime
from sqlalchemy import or_, and_

# app = Flask(__name__)
os.environ['DATABASE_URL'] =  'postgres://jizezwuvqqqggm:2d53be5d779c2ce5ee025fb9a173a13d17c5c63341dd8976c1a363d52732b2d9@ec2-54-159-175-113.compute-1.amazonaws.com:5432/dd5q43uk9mpsk0'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/register", methods=["GET","POST"])
def register():
    # print(SELECT *FROM users)
    data = Users.query.all()
    print(data)
    msg = ""
    if (request.method=="POST"):
        name = request.form.get("name")
        pwd = request.form.get("pwd")
        timestamp = datetime.datetime.now()
        try:
            new_user = Users(email = name, password = pwd, timestamp = timestamp)
            if(name == '' or pwd == ''):
                msg = "Email or password could not be empty"
                return render_template("Register.html", message = msg)
            else:
                db.add(new_user)
                db.commit()
                msg = "Registration was completed. Please Login"
                return render_template("Register.html", message = msg)

        except:
            msg = "You already registered with this email id. Please Login"
            return render_template("Register.html", message = msg)
    else:
        return render_template("Register.html")

@app.route("/login", methods=['POST','GET'])
def authenticate():
    print("hello")
    if request.method == 'POST':
        email = request.form.get("name")
        password = request.form.get("pwd")
        
        data = Users.query.get(email)
        print(data)
        if data != None:
            print(data)
            print(password == data.password)
            if password == data.password:
                # session["email"] = email
                print("data_2")
                return render_template("home.html", email = session.get("email"))
            else:
                return render_template("Register.html", message="Incorrect password")
        else:
            return render_template("Register.html", message="Invalid email")
    else:
        if session.get("email") is None:
            return render_template('Register.html')
    return render_template("home2.html", email = session.get("email"))

@app.route("/logout")
def logout():
    session.clear()
    return render_template("Register.html")
if __name__ == '__main__':
    app.debug = True
    app.run()