from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_classes.base import Base
from orm_classes.tenant import Tenant
from DummyData import dummydata
from passlib.hash import bcrypt
from orm_classes.listing import Listing
from orm_classes.application import Application
from orm_classes.reference import Reference
from orm_classes.property import Property
from orm_classes.referee import Referee
from orm_classes.landlord import Landlord

engine = create_engine('mysql://be120c56a36647:1cd891e0@us-cdbr-iron-east-05.cleardb.net/heroku_1ce649df9303ad6',
                       echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#phash = bcrypt.genhash()
password = b"password"
phash = bcrypt.using(rounds=13).hash(password)
phash = bytearray(phash, 'utf-8')

print(dummydata.emailList[1])
new_tenant = Tenant()
new_tenant.fname = 'Dylan'
new_tenant.lname = 'Watson'
new_tenant.phone = '01212'
new_tenant.email = dummydata.emailList[1]
new_tenant.hash = phash
new_tenant.profile_picture = 'test'
new_tenant.payment_method = 'test'
new_tenant.payment_token = 'test'

new_tenant.__repr__()

session.add(new_tenant)
session.commit()
