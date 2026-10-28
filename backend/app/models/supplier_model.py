from pydantic import BaseModel, EmailStr
from typing import Optional


class SupplierCreate(BaseModel):
    name: str
    contact_person: str
    phone: str
    email: EmailStr
    address: str


class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None