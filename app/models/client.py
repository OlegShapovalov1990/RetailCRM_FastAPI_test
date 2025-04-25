from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Phone(BaseModel):
    number: str


class CustomerCreate(BaseModel):
    site: Optional[str] = None
    firstName: str
    lastName: str
    phones: List[Phone]
    email: Optional[str] = None
    # Добавляем все возможные поля из документации
    externalId: Optional[str] = None
    patronymic: Optional[str] = None
    birthday: Optional[datetime] = None
    managerId: Optional[int] = None


class CustomerResponse(BaseModel):
    success: bool
    id: Optional[int] = None
    errorMsg: Optional[str] = None

    class Config:
        extra = "ignore"