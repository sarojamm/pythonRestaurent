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

myFirstRestaurant = Restaurant(name = "Pizza Place")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
session.query(Restaurant).first().name

cheesepizza = MenuItem(name =" Cheese Pizza" , description = " Made with all natural ingredients and fresh mozzarella", course =" Entree", price="$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
session.query(MenuItem).first().name

