from pydantic import BaseModel
from typing import Optional


class PurchaseOrderCreate(BaseModel):
    supplier_id: str
    ingredient_name: str
    quantity: float
    unit: str
    status: str = "pending"


class PurchaseOrderUpdate(BaseModel):
    supplier_id: Optional[str] = None
    ingredient_name: Optional[str] = None
    quantity: Optional[float] = None
    unit: Optional[str] = None
    status: Optional[str] = None