from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class PartialUpdateProduct(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    stock: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
