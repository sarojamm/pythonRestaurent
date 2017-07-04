import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine) 
session = DBSession()
##### Create 
myFirstRestaurant = Restaurant(name = "Pizza Place")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
session.query(Restaurant).first().name
## create a cheese pizza menu item and added it to the Pizza Palace Menu:
cheesepizza = MenuItem(name =" Cheese Pizza" , description = " Made with all natural ingredients and fresh mozzarella", course =" Entree", price="$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
session.query(MenuItem).first().name
# READ We read out information in our database using the query method in SQLAlchemy:
firstResult = session.query(Restaurant).first()
firstResult.name

items = session.query(MenuItem).all()
for item in items:
    print item.name

#found the veggie burger that belonged to the Urban Burger restaurant by executing the following query:
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit() 


### DELETE

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit() 
