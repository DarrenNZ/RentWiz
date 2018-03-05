import MySQLdb
from sqlalchemy import*
from sqlalchemy.ext.declarative import*
from sqlalchemy.orm import relationship
from sqlalchemy.orm import*


# if __name__ == '__main__':
#     app.run()

from orm_classes.base import Base
from orm_classes.tenant import Tenant
from orm_classes.application import Application
from orm_classes.landlord import Landlord
from orm_classes.listing import Listing
from orm_classes.property import Property
from orm_classes.reference import Reference
from orm_classes.referee import Referee

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#                            Association
#     person = relationship("Person", back_populates= "addresses")


engine = create_engine('mysql://be120c56a36647:1cd891e0@us-cdbr-iron-east-05.cleardb.net/heroku_1ce649df9303ad6', echo = True)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)