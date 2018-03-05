import MySQLdb
from sqlalchemy import*
from sqlalchemy.ext.declarative import*
from sqlalchemy.orm import relationship
from sqlalchemy.orm import*

from orm_classes.base import Base
from orm_classes.tenant import Tenant
from orm_classes.application import Application
from orm_classes.landlord import Landlord
from orm_classes.listing import Listing
from orm_classes.property import Property
from orm_classes.reference import Reference
from orm_classes.referee import Referee

engine = create_engine('mysql://be120c56a36647:1cd891e0@us-cdbr-iron-east-05.cleardb.net/heroku_1ce649df9303ad6', echo = True)
Base.metadata.drop_all(engine)