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
@app.route('/locations/')
def locations():
    users = session.query(User).all()
    categories = session.query(Category).all()
    session.close()
    return render_template('locations.html', users = users, categories = categories)


@app.route('/locations/<int:cat_id>/')
def location(cat_id):
    return render_template('location.html', cat_id = cat_id)


@app.route('/locations/add')
def addLocation():
    return render_template('location_add.html')


@app.route('/locations/<int:cat_id>/edit')
def editLocation(cat_id):
    return render_template('location_edit.html', cat_id = cat_id)


@app.route('/locations/<int:cat_id>/wall-<int:wall_id>/')
def wall(cat_id, wall_id):
    return render_template('wall.html', cat_id = cat_id, wall_id = wall_id)


@app.route('/locations/<int:cat_id>/wall/add')
def addWall(cat_id):
    return render_template('wall_add.html', cat_id = cat_id)


@app.route('/locations/<int:cat_id>/wall-<int:wall_id>/edit')
def editWall(cat_id, wall_id):
    return render_template('wall_edit.html', cat_id = cat_id, wall_id = wall_id)



# If you're executing me from the Python interpreter, do this:
# If you're importing this file, don't do this:
if __name__ == '__main__':
    # app.debug = True triggers a server reboot of sorts
    # if a change in the code is detected
    # as well as providing a debugger on the page
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
