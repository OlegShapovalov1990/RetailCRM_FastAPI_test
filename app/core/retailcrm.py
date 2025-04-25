import httpx
from httpx import Response
from ..core.config import settings


class RetailCRMClient:
    def __init__(self):
        self.base_url = settings.retailcrm_api_url
        self.api_key = settings.retailcrm_api_key
        self.client = httpx.AsyncClient()

    async def _request(self, method: str, endpoint: str, params: dict = None, json: dict = None) -> Response:
        url = f"{self.base_url}/api/v5/{endpoint}"
        params = params or {}
        params["apiKey"] = self.api_key

        return await self.client.request(
            method=method,
            url=url,
            params=params,
            json=json,
            timeout=30.0
        )

    async def get_customers(self, filters: dict = None) -> Response:
        return await self._request("GET", "customers", params=filters)

    async def create_customer(self, customer_data: dict) -> Response:
        return await self._request("POST", "customers/create", json=customer_data)

    async def get_orders(self, filters: dict = None) -> Response:
        return await self._request("GET", "orders", params=filters)

    async def create_order(self, order_data: dict) -> Response:
        return await self._request("POST", "orders/create", json=order_data)

    async def create_payment(self, payment_data: dict) -> Response:
        return await self._request("POST", "orders/payments/create", json=payment_data)


retailcrm_client = RetailCRMClient()