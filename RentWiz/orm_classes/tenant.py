from sqlalchemy import *
from sqlalchemy.ext.declarative import *

from orm_classes.base import Base
from sqlalchemy.orm import relationship
from orm_classes.application import Application

#this is the entity and ORM object representing a tenant
class Tenant(Base):
    __tablename__ = 'Tenant'

    tenant_id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50))
    lname = Column(String(50))
    phone = Column(String(11))
    email = Column(String(254), nullable=False)
    hash = Column(Binary(60), nullable=False)
    profile_picture = Column(String(260))
    payment_method = Column(String(20))
    payment_token = Column(String(150))

    references = relationship("Reference", back_populates='tenant')
    applications = relationship("Application", back_populates='tenant')

    def __repr__(self):
        return "<Tenant(tenant_id='%s'," \
               " fname='%s', lname='%s', phone='%s', " \
               "email='%s', hash='%s', profile_picture='%s', " \
               "payment_method='%s', payment_token='%s')>" \
               % (self.tenant_id, self.fname, self.lname, self.phone,
                  self.email, self.hash, self.profile_picture,
                  self.payment_method, self.payment_token)

   # def __init__(self):