from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base


class Product(Base):
    __tablename__ = "products"

    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    order_items = relationship("OrderItem", back_populates="product")
