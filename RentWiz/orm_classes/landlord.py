from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from orm_classes.base import Base
from sqlalchemy.orm import relationship


#this is the entity and ORM object representing a landlord
class Landlord(Base):
    __tablename__ = 'Landlord'

    landlord_id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50))
    lname = Column(String(50))
    phone = Column(String(11))
    email = Column(String(254), nullable=False)
    hash = Column(Binary(60), nullable=False)
    profile_picture = Column(String(260))

    properties = relationship("Property", back_populates = 'landlord')

    def __repr__(self):
        return "<Landlord(landlord_id='%s'," \
               " fname='%s', lname='%s', phone='%s', " \
               "email='%s', hash='%s', profile_picture='%s')>" \
               % (self.landlord_id, self.fname, self.lname, self.phone,
                  self.email, self.hash, self.profile_picture)