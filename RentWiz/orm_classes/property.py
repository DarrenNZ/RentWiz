from sqlalchemy import *
from sqlalchemy.ext.declarative import *
import datetime

from orm_classes.base import Base
from sqlalchemy.orm import relationship

#this is the entity and ORM object representing a property
class Property(Base):
    __tablename__ = 'Property'

    property_id = Column(Integer, primary_key=True, autoincrement=True)
    address_line_one = Column(String(50), nullable=false)
    address_line_two = Column(String(50), nullable=false)
    postcode = Column(String(10))
    bathrooms = Column(Integer)
    tenant_capacity = Column(Integer)
    bedrooms = Column(Integer)
    longitude = Column(Numeric(precision=10, scale=7))
    latitude = Column(Numeric(precision=10, scale=7))
    date_added = Column(Date, default=datetime.datetime.now())
    date_sold = Column(Date)

    landlord_id = Column(Integer, ForeignKey('Landlord.landlord_id'))
    #listing_id = Column(Integer, ForeignKey('Listing.listing_id'))

    listings = relationship("Listing", back_populates = 'property')
    landlord = relationship("Landlord", back_populates = 'properties')


    def __repr__(self):
        return "<Property(property_id = '%s'," \
               " address line one = '%s', address line two = '%s', post code = '%s', bathrooms = '%s', " \
               "tenant_capacity = '%s', bedrooms = '%s', " \
               "longitude = '%s', latitude = '%s', " \
               "date_added = '%s', date_sold = '%s')>" \
               % (self.property_id, self.address_line_one, self.address_line_two, self.postcode, self.bathrooms,
                  self.tenant_capacity, self.bedrooms, self.longitude, self.latitude
                  , self.date_added, self.date_sold)
