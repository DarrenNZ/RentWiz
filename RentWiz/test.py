from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://be120c56a36647:1cd891e0@us-cdbr-iron-east-05.cleardb.net/heroku_1ce649df9303ad6', echo=True)

Base = declarative_base()

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

    def __repr__(self):
        return "<Tenant(tenant_id='%s', fname='%s', lname='%s', phone='%s', email='%s', hash='%s', profile_picture='%s', payment_method='%s', payment_token='%s')>" % (self.tenant_id, self.fname, self.lname, self.phone, self.email, self.hash, self.profile_picture, self.payment_method, self.payment_token)

Base.metadata.create_all(engine)