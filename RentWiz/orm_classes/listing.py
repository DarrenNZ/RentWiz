from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import relationship

from orm_classes.base import Base


class Listing(Base):
    __tablename__ = 'Listing'

    listing_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(140))
    price = Column(Integer)
    num_rooms = Column(Integer)
    num_tenants = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Integer)
    feedback = Column(String(140))

    property_id = Column(Integer, ForeignKey('Property.property_id'))
    #application_id = Column(Integer, ForeignKey('Application.application_id'))

    applications = relationship('Application', back_populates = 'listing')
    property = relationship('Property', foreign_keys = [property_id], back_populates = 'listings')


