from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import relationship
from orm_classes.base import Base

class Reference(Base):
    __tablename__ = 'Reference'

    reference_id = Column(Integer, primary_key=True, autoincrement= True)
    type = Column(Integer)
    description = Column(String(140))
    referee_id = Column(Integer, ForeignKey('Referee.referee_id'))
    tenant_id = Column(Integer, ForeignKey('Tenant.tenant_id'))

    referee = relationship("Referee", back_populates = 'references')
    tenant = relationship("Tenant", back_populates = 'references')

