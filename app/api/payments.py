from fastapi import APIRouter, Depends, HTTPException
from ..models.payment import Payment, PaymentCreate
from ..core.retailcrm import retailcrm_client

router = APIRouter()


@router.post("/", response_model=Payment)
async def create_payment(payment: PaymentCreate):
    payment_data = {
        "order": {"id": payment.order_id},
        "amount": payment.amount,
        "type": payment.type,
        "status": payment.status
    }

    response = await retailcrm_client.create_payment({"payment": payment_data})
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json().get("payment")