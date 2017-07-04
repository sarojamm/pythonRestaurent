from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine) 
session = DBSession()



app = Flask(__name__)

@app.route('/')
@app.route('/restaurants') 
def helloworld():
	#restaurant = session.query(Restaurant).filter_by(id = restaurant_id) 
    restaurant = session.query(Restaurant).first()
    restaurants = session.query(Restaurant).all()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)

    output = ""
    output += "<html><body>"
    output += "<a href='/restaurants/new'> Restaurant New </a> "
    output += " | <a href='/restaurants/%s/edit'> Restaurant Edit </a> " % restaurant.id
    output += " | <a href='/restaurants/%s/delete'> Restaurant Delete</a> " % restaurant.id
    output += " | <a href='/restaurants'> Restaurant View</a> "
    output += " </br></br>"

    output += ""
    for item in items:
        output += item.name
        output += " - " + item.price
        output += "</br>"
    output += " <a href='/restaurants/new' > Create a New Restaurant</a></p>"
    for restaurant in restaurants:
        output += restaurant.name
        output += "<a href='/restaurants/%s/edit'> Edit</a> " % restaurant.id
        output += " | <a href='/restaurants/%s/delete'> Delete</a> " % restaurant.id
        output += " | <a href='/restaurants/%s'> Menu</a> " % restaurant.id
        output += " </br>"
        output += "</body></html>"
    return output


@app.route('/restaurants/<int:restaurant_id>/') 
def restaurantmenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id ).one()
    #restaurants = session.query(Restaurant).all()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    output = ""
    output += "<html><body>"
    for item in items:
        output += item.name
        output += " - " + item.price
        output += "</br>"
    output += " <a href='/restaurants/new' > Create a New Restaurant</a></p>"
    restaurants = session.query(Restaurant).all()
    for restaurant1 in restaurants:
        output += restaurant1.name
        output += "<a href='/restaurants/%s/edit'> Edit</a> " % restaurant1.id
        output += " | <a href='/restaurants/%s/delete'> Delete</a> " % restaurant1.id
        output += " | <a href='/restaurants/%s'> Menu</a> " % restaurant1.id
        output += " </br>"
        output += "</body></html>"
    return output
@app.route('/restaurants/new')
def newRestaurentItem():
    return " page to create  a new restaurant "
@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurentItem(restaurant_id ):
    return " page to edit  a new restaurant "
@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurentItem(restaurant_id ):
    return " page to delete  a new restaurant "

@app.route('/menus/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
    return " page to create  a new menu Item"
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "Page to edit a menu item ."
@app.route('/menus/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "Page to delete a menu Item."

if __name__ == '__main__':
	app.debug = True
	app.run(host = 'localhost', port = 8080)