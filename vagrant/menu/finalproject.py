from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This page will show all my restaurants"


@app.route('/restaurant/new')
def newRestaurant():
    return "This page will be for making a new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page will be for editing restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page will be for deleting restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return "This page will be for showing menu for restaurant {}".format(restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "This page will be for making a new menu item in restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page will be for editing menu item {} in restaurant {}".format(menu_id, restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "This page will be for deleting menu item {} in restaurant {}".format(menu_id, restaurant_id)


# If you're executing me from the Python interpreter, do this:
# If you're importing this file, don't do this:
if __name__ == '__main__':
    # app.debug = True triggers a server reboot of sorts
    # if a change in the code is detected
    # as well as providing a debugger on the page
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
