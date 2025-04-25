from pydantic import BaseModel


class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    type: str = "cash"
    status: str = "paid"


class Payment(BaseModel):
    id: int
    amount: float
    orderId: int

    class Config:
        from_attributes = True