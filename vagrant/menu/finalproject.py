from flask import Flask, render_template
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    # return "This page will show all my restaurants"
    return render_template('restaurants.html', restaurants = restaurants)


@app.route('/restaurant/new')
def newRestaurant():
    # return "This page will be for making a new restaurant"
    return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    # return "This page will be for editing restaurant {}".format(restaurant_id)
    return render_template('editRestaurant.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    # return "This page will be for deleting restaurant {}".format(restaurant_id)
    return render_template('deleteRestaurant.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    # return "This page will be for showing menu for restaurant {}".format(restaurant_id)
    return render_template('menu.html', restaurant = restaurant, items = items)


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    # return "This page will be for making a new menu item in restaurant {}".format(restaurant_id)
    return render_template('newMenuItem.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    # return "This page will be for editing menu item {} in restaurant {}".format(menu_id, restaurant_id)
    return render_template('editMenuItem.html', item = item, restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
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
