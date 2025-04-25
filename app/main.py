from fastapi import FastAPI
from .api import clients, orders, payments

app = FastAPI(
    title="RetailCRM FastAPI Integration",
    description="API для интеграции с RetailCRM",
    version="0.1.0",
)

app.include_router(clients.router)
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["payments"])

@app.get("/")
async def root():
    return {"message": "RetailCRM FastAPI Integration"}