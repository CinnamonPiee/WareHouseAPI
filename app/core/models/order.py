from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base
import enum


class OrderStatus(str, enum.Enum):
    in_progress = "in_progress"
    sent = "sent"
    delivered = "delivered"


class Order(Base):
    __tablename__ = "orders"

    created_at = Column(DateTime, server_default=func.now())
    status = Column(Enum(OrderStatus), default=OrderStatus.in_progress)

    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
