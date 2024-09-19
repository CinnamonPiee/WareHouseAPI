from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Product(Base):
    __tablename__ = "product"

    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
