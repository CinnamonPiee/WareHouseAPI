from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    created_at: datetime
    status: Optional[str] = "in process"


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
