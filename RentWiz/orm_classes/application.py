from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from orm_classes.base import Base
from sqlalchemy.orm import relationship
#from orm_classes.listing import Listing
#from orm_classes.tenant import Tenant


class Application(Base):
    __tablename__ = 'Application'

    application_id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(140))
    listing_id = Column(Integer, ForeignKey("Listing.listing_id"))
    tenant_id = Column(Integer, ForeignKey("Tenant.tenant_id"))
    status = Column(Integer)


    listing = relationship("Listing", foreign_keys = [listing_id], back_populates ="applications")
    tenant = relationship("Tenant", foreign_keys = [tenant_id],back_populates ="applications")

