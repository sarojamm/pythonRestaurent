import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

########
class  Employee(Base):
	__tablename__ = 'employee'

	name = Column( String(80), nullable = False)
	id = Column( Integer, primary_key = True)

	"""docstring for  Restaurant"""
	
	def __init__(self, arg):
		super( Employee, self).__init__()
		self.arg = arg
class Address(Base):
	__tablename__ = 'address'

	street = Column(String (80), nullable = False)

	id = Column(Integer, primary_key = True)
	zip = Column(String(5)) 
	employee_id = Column(
 		Integer, ForeignKey('employee.id'))

	employee = relationship(Employee)
	"""docstring for MenuItem"""
	def __init__(self, arg):
		super(Address, self).__init__()
		self.arg = arg
		

#######
############# insert at end of the file. #####
######## engine = create_engine(
 ##               "mysql://root:2552amantea@localhost/restaurantmenu.db" 
  ###          ) #########
engine = create_engine("sqlite:///employeeData.db")
Base.metadata.create_all(engine)