from flask import Flask , render_template, request, redirect, url_for
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
def restaurants():
	#restaurant = session.query(Restaurant).filter_by(id = restaurant_id) 
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)
@app.route('/restaurants/<int:restaurant_id>/') 
def restaurantmenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id ).one()
    #restaurants = session.query(Restaurant).all()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    restaurants = session.query(Restaurant).all( )
    return render_template('menu.html', restaurants=restaurants, restaurant=restaurant, items=items)
@app.route('/restaurants/new' , methods=['GET','POST'])
def newRestaurentItem():
    if(request.method == 'POST'):
        newrestaurent = Restaurant(name = request.form['restaurantname'])
        session.add(newrestaurent)
        session.commit()
        return redirect(url_for('restaurants'))
    else:
        return render_template('newrestaurant.html')
@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurentItem(restaurant_id ):
    return " page to edit  a new restaurant "
@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurentItem(restaurant_id ):
    delrestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if(request.method == 'POST'):
        session.delete(delrestaurant)
        session.commit()
        return redirect(url_for('restaurants'))
    else:
        return render_template('deleteRestaurent.html',item = delrestaurant)

@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    if(request.method == 'POST'):
        newMenuItem = MenuItem(name = request.form['menuname'],description=request.form['menudescription'],
                               price=request.form['price'],course="Appetizer", restaurant_id = restaurant_id)
        session.add(newMenuItem)
        session.commit()
        return redirect(url_for('restaurantmenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html' ,restaurant_id=restaurant_id)
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "Page to edit a menu item ."
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete' , methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    delmenuitem = session.query(MenuItem).filter_by(id=menu_id).one()
    if (request.method == 'POST'):
        session.delete(delmenuitem)
        session.commit()
        return redirect(url_for('restaurantmenu',
                                restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=delmenuitem)

if __name__ == '__main__':
	app.debug = True
	app.run(host = 'localhost', port = 8080)