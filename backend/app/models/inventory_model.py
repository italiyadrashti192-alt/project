# from pydantic import BaseModel


# class InventoryCreate(BaseModel):
#     ingredient_id: str
#     quantity: float
#     unit: str
#     minimum_stock: float

# from pydantic import BaseModel, Field
# from typing import Optional


# class InventoryCreate(BaseModel):
#     ingredient_name: str
#     quantity: float
#     unit: str
#     minimum_stock: float = 0


# class InventoryUpdate(BaseModel):
#     ingredient_name: Optional[str] = None
#     quantity: Optional[float] = None
#     unit: Optional[str] = None
#     minimum_stock: Optional[float] = None

# from pydantic import BaseModel, Field
# from typing import Optional


# class InventoryCreate(BaseModel):

#     ingredient_name: str = Field(..., min_length=2)

#     quantity: float = Field(..., ge=0)

#     unit: str

#     minimum_stock: float = Field(..., ge=0)

#     supplier: Optional[str] = None


# class InventoryUpdate(BaseModel):

#     ingredient_name: Optional[str] = None

#     quantity: Optional[float] = Field(None, ge=0)

#     unit: Optional[str] = None

#     minimum_stock: Optional[float] = Field(None, ge=0)

#     supplier: Optional[str] = None

from pydantic import BaseModel, Field
from typing import Optional


class InventoryCreate(BaseModel):

    ingredient_name: str = Field(..., min_length=2)

    quantity: float = Field(..., ge=0)

    unit: str

    minimum_stock: float = Field(..., ge=0)

    # Store Supplier MongoDB ObjectId as a string
    supplier_id: Optional[str] = None


class InventoryUpdate(BaseModel):

    ingredient_name: Optional[str] = None

    quantity: Optional[float] = Field(None, ge=0)

    unit: Optional[str] = None

    minimum_stock: Optional[float] = Field(None, ge=0)

    # Store Supplier MongoDB ObjectId as a string
    supplier_id: Optional[str] = None