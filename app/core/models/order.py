from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base


class Order(Base):
    __tablename__ = "order"

    created_at = Column(DateTime)
    status = Column(String, default="in process")


class OrderItem(Base):
    __tablename__ = "order_item"

    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")
