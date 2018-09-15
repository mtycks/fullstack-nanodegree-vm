from flask import Flask
app = Flask(__name__)

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to # DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = create_engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '<br />'
        output += i.price
        output += '<br />'
        output += i.description
        output += '<br /><br />'
    return output


# If you're executing me from the Python interpreter, do this:
# If you're importing this file, don't do this:
if __name__ == '__main__':
    # app.debug = True triggers a server reboot of sorts
    # if a change in the code is detected
    # as well as providing a debugger on the page
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
