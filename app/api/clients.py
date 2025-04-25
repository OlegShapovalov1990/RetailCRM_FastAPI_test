from fastapi import APIRouter, HTTPException, status
from ..models.client import CustomerCreate, CustomerResponse
from ..core.retailcrm import retailcrm_client
import logging
from datetime import datetime
from typing import Optional, List

router = APIRouter(prefix="/customers", tags=["customers"])
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[CustomerResponse])
async def get_customers(firstName: Optional[str] = None,
                        lastName: Optional[str] = None,
                        email: Optional[str] = None):
    try:
        filters = {}
        if firstName:
            filters["firstName"] = firstName
        if lastName:
            filters["lastName"] = lastName
        if email:
            filters["email"] = email

        response = await retailcrm_client.get_customers(filters)
        response.raise_for_status()

        crm_response = response.json()
        if not crm_response.get("success"):
            raise HTTPException(status_code=400, detail=crm_response.get("errorMsg", "Unknown error"))

        return [
            CustomerResponse(
                id=c.get("id"),
                firstName=c.get("firstName"),
                lastName=c.get("lastName"),
                createdAt=c.get("createdAt")
            )
            for c in crm_response.get("customers", [])
        ]

    except Exception as e:
        logger.error(f"Error fetching customers: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))







@router.post("/",
             response_model=CustomerResponse,
             status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate):
    try:
        # Подготовка данных строго по документации RetailCRM
        customer_data = {
            "firstName": customer.firstName,
            "lastName": customer.lastName,
            "phones": [{"number": phone.number} for phone in customer.phones],
        }

        # Добавляем опциональные поля
        if customer.email:
            customer_data["email"] = customer.email
        if customer.externalId:
            customer_data["externalId"] = customer.externalId
        if customer.patronymic:
            customer_data["patronymic"] = customer.patronymic
        if customer.birthday:
            customer_data["birthday"] = customer.birthday.isoformat()
        if customer.managerId:
            customer_data["managerId"] = customer.managerId

        # Подготовка полного запроса
        request_data = {"customer": customer_data}
        if customer.site:
            request_data["site"] = customer.site

        # Отправка в RetailCRM
        response = await retailcrm_client.create_customer(request_data)

        # Обработка ответа
        crm_response = response.json()

        # Возвращаем ответ в точности как RetailCRM
        return CustomerResponse(
            success=crm_response.get("success", False),
            id=crm_response.get("id"),
            errorMsg=crm_response.get("errorMsg")
        )

    except Exception as e:
        logger.error(f"Error creating customer: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )