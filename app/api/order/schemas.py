from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from enum import Enum


class OrderBase(BaseModel):
    status: Optional[str] = "in process"


class OrderCreate(OrderBase):
    pass


class OrderStatusUpdate(BaseModel):
    status: str


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    model_config = ConfigDict(from_attributes=True)


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    order_items: List[OrderItem] = []
