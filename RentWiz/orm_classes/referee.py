from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from orm_classes.base import Base
from sqlalchemy.orm import relationship

class Referee(Base):
    __tablename__ = 'Referee'

    referee_id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50))
    lname = Column(String(50))
    phone = Column(String(11), nullable=false)
    email = Column(String(254), nullable=False)
    hash = Column(Binary(60))

    references = relationship("Reference", back_populates = 'referee')
