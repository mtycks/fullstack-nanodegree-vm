#!/usr/bin/env python2.7

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)

# import CRUD Operations from Lesson 1
from models import Base, User, Category, Wall, WallPhoto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to # DB
engine = create_engine('sqlite:///waldir.db')
Base.metadata.bind = create_engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def homepage():
    return render_template('homepage.html')



# If you're executing me from the Python interpreter, do this:
# If you're importing this file, don't do this:
if __name__ == '__main__':
    # app.debug = True triggers a server reboot of sorts
    # if a change in the code is detected
    # as well as providing a debugger on the page
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
