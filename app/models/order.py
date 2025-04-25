from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class OrderItem(BaseModel):
    offer: dict
    quantity: int


class OrderCreate(BaseModel):
    number: str
    customer: dict
    items: List[OrderItem]


class Order(BaseModel):
    id: int
    number: str
    createdAt: datetime
    customerId: Optional[int]

    class Config:
        from_attributes = True