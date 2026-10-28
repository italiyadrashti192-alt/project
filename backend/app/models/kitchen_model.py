# from pydantic import BaseModel
# from typing import Optional


# class KitchenCreate(BaseModel):
#     order_id: str
#     food_name: str
#     quantity: int
#     status: str = "pending"
#     estimated_time: int


# class KitchenUpdate(BaseModel):
#     order_id: Optional[str] = None
#     food_name: Optional[str] = None
#     quantity: Optional[int] = None
#     status: Optional[str] = None
#     estimated_time: Optional[int] = None


# from pydantic import BaseModel, Field
# from typing import Optional, List
# from datetime import datetime



# # =========================================================
# # INGREDIENT REQUIRED FOR KITCHEN ORDER
# # =========================================================
# class KitchenIngredient(BaseModel):
#     ingredient_name: str
#     quantity_required: float
#     unit: str


# # =========================================================
# # CREATE KITCHEN ORDER
# # =========================================================
# class KitchenCreate(BaseModel):
#     order_id: str
#     food_name: str
#     quantity: int
#     status: str = "pending"
#     estimated_time: int
#     ingredients: List[KitchenIngredient]
#     order_date: datetime = Field(default_factory=datetime.now)
#     # Field(default_factory=datetime.now)
#     ingredients: List[KitchenIngredient]


# # =========================================================
# # UPDATE KITCHEN ORDER
# # =========================================================
# class KitchenUpdate(BaseModel):
#     order_id: Optional[str] = None
#     food_name: Optional[str] = None
#     quantity: Optional[int] = None
#     status: Optional[str] = None
#     estimated_time: Optional[int] = None
#     ingredients: Optional[List[KitchenIngredient]] = None
#     order_date: Optional[datetime] = None
#     ingredients: Optional[List[KitchenIngredient]] = None



from pydantic import BaseModel, Field
from typing import List


class KitchenIngredient(BaseModel):
    ingredient_name: str
    quantity_required: float = Field(..., ge=0)
    unit: str


class KitchenCreate(BaseModel):
    order_id: str
    food_name: str
    quantity: int = Field(..., ge=1)
    status: str = "pending"
    estimated_time: int = Field(..., ge=0)
    ingredients: List[KitchenIngredient]


class KitchenUpdate(BaseModel):
    order_id: str | None = None
    food_name: str | None = None
    quantity: int | None = Field(None, ge=1)
    status: str | None = None
    estimated_time: int | None = Field(None, ge=0)
    ingredients: List[KitchenIngredient] | None = None