from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = session.query(Restaurant).order_by(Restaurant.name).all()
    session.close()
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        # Create the variable to hold the data from the POST
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):

    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    session.close()

    if request.method == 'POST':

        # Create the variable to update the restaurant
        # restaurant = session.query(Restaurant).filter_by(restaurant_id = restaurant.id)
        if request.form['name']:
            restaurant.name = request.form['name']
        session.add(restaurant)
        session.commit()
        session.close()
        return redirect(url_for('showRestaurants'))

    else:
        return render_template('editRestaurant.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    session.close()

    if request.method == 'POST':
        session.delete(restaurant)
        session.commit()
        session.close()

        return redirect(url_for('showRestaurants'))

    else:
        return render_template('deleteRestaurant.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/', methods=['GET', 'POST'])
@app.route('/restaurant/<int:restaurant_id>/menu', methods=['GET', 'POST'])
def showMenu(restaurant_id):

    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    session.close()

    return render_template('menu.html', items = items, restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    # return "This page will be for making a new menu item in restaurant {}".format(restaurant_id)
    return render_template('newMenuItem.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    session.close()

    if request.method == 'POST':
        # Create the variable to update the restaurant
        # restaurant = session.query(Restaurant).filter_by(restaurant_id = restaurant.id)
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['price']:
            item.price = request.form['price']
        if request.form['course']:
            item.course = request.form['course']
        session.add(item)
        session.commit()
        session.close()
        return redirect(url_for('showMenu', restaurant_id = restaurant_id ))

    else:
        return render_template('editMenuItem.html', item = item, restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    # return "This page will be for deleting menu item {} in restaurant {}".format(menu_id, restaurant_id)
    return render_template('deleteMenuItem.html', item = item, restaurant = restaurant)


# If you're executing me from the Python interpreter, do this:
# If you're importing this file, don't do this:
if __name__ == '__main__':
    # app.debug = True triggers a server reboot of sorts
    # if a change in the code is detected
    # as well as providing a debugger on the page
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
