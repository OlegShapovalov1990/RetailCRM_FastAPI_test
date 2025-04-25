from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.order import Order, OrderCreate
from ..core.retailcrm import retailcrm_client

router = APIRouter()


@router.get("/customer/{customer_id}", response_model=List[Order])
async def get_customer_orders(customer_id: int):
    response = await retailcrm_client.get_orders({"customerId": customer_id})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json().get("orders", [])


@router.post("/", response_model=Order)
async def create_order(order: OrderCreate):
    order_data = {
        "number": order.number,
        "customer": order.customer,
        "items": [item.dict() for item in order.items]
    }

    response = await retailcrm_client.create_order({"order": order_data})
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json().get("order")