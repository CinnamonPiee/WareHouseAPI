from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    created_at: datetime
    status: Optional[str] = "in process"


class OrderStatusUpdate(BaseModel):
    status: str


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)
