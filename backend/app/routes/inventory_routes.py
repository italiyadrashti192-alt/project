# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# @router.get("/")
# def get_inventory():
#     return {
#         "status": "success",
#         "message": "Inventory API is working"
#     }

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from bson import ObjectId

# # from app.database import db


# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# # =========================================================
# # Inventory Model
# # =========================================================

# class Inventory(BaseModel):
#     ingredient_id: str
#     quantity: float
#     unit: str
#     minimum_stock: float = 0
#     location: Optional[str] = None


# # =========================================================
# # GET - Get All Inventory
# # =========================================================

# @router.get("/")
# def get_inventory():

#     inventory = list(db["inventory"].find())

#     for item in inventory:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(inventory),
#         "inventory": inventory
#     }


# # =========================================================
# # POST - Add Inventory
# # =========================================================

# @router.post("/")
# def add_inventory(data: Inventory):

#     # Check whether ingredient exists
#     ingredient = db["ingredients"].find_one(
#         {"_id": ObjectId(data.ingredient_id)}
#     )

#     if not ingredient:
#         raise HTTPException(
#             status_code=404,
#             detail="Ingredient not found"
#         )

#     inventory_data = {
#         "ingredient_id": data.ingredient_id,
#         "ingredient_name": ingredient["name"],
#         "quantity": data.quantity,
#         "unit": data.unit,
#         "minimum_stock": data.minimum_stock,
#         "location": data.location
#     }

#     result = db["inventory"].insert_one(inventory_data)

#     return {
#         "status": "success",
#         "message": "Inventory added successfully",
#         "inventory_id": str(result.inserted_id)
#     }


# # =========================================================
# # PUT - Update Inventory
# # =========================================================

# @router.put("/{inventory_id}")
# def update_inventory(
#     inventory_id: str,
#     data: Inventory
# ):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     existing_inventory = db["inventory"].find_one(
#         {"_id": ObjectId(inventory_id)}
#     )

#     if not existing_inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     ingredient = db["ingredients"].find_one(
#         {"_id": ObjectId(data.ingredient_id)}
#     )

#     if not ingredient:
#         raise HTTPException(
#             status_code=404,
#             detail="Ingredient not found"
#         )

#     update_data = {
#         "ingredient_id": data.ingredient_id,
#         "ingredient_name": ingredient["name"],
#         "quantity": data.quantity,
#         "unit": data.unit,
#         "minimum_stock": data.minimum_stock,
#         "location": data.location
#     }

#     db["inventory"].update_one(
#         {"_id": ObjectId(inventory_id)},
#         {"$set": update_data}
#     )

#     return {
#         "status": "success",
#         "message": "Inventory updated successfully"
#     }


# # =========================================================
# # DELETE - Delete Inventory
# # =========================================================

# @router.delete("/{inventory_id}")
# def delete_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     result = db["inventory"].delete_one(
#         {"_id": ObjectId(inventory_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory deleted successfully"
#     }

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from bson import ObjectId

# from app.db_config import db


# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# # =========================================================
# # Inventory Model
# # =========================================================

# class Inventory(BaseModel):
#     ingredient_id: str
#     quantity: float
#     unit: str
#     minimum_stock: float = 0
#     location: Optional[str] = None


# # =========================================================
# # GET - Get All Inventory
# # =========================================================

# @router.get("/")
# def get_inventory():

#     inventory_collection = db["inventory"]

#     inventory = list(inventory_collection.find())

#     for item in inventory:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(inventory),
#         "inventory": inventory
#     }


# # =========================================================
# # POST - Add Inventory
# # =========================================================

# @router.post("/")
# def add_inventory(data: Inventory):

#     ingredients_collection = db["ingredients"]
#     inventory_collection = db["inventory"]

#     # Check ingredient ID
#     if not ObjectId.is_valid(data.ingredient_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid ingredient ID"
#         )

#     # Check ingredient exists
#     ingredient = ingredients_collection.find_one(
#         {"_id": ObjectId(data.ingredient_id)}
#     )

#     if not ingredient:
#         raise HTTPException(
#             status_code=404,
#             detail="Ingredient not found"
#         )

#     inventory_data = {
#         "ingredient_id": data.ingredient_id,
#         "ingredient_name": ingredient["name"],
#         "quantity": data.quantity,
#         "unit": data.unit,
#         "minimum_stock": data.minimum_stock,
#         "location": data.location
#     }

#     result = inventory_collection.insert_one(inventory_data)

#     return {
#         "status": "success",
#         "message": "Inventory added successfully",
#         "inventory_id": str(result.inserted_id)
#     }

# # =========================================================
# # GET - Add Inventory
# # =========================================================

# @router.get("/")
# def get_inventory():
#     inventory = list(inventory_collection.find())

#     for item in inventory:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(inventory),
#         "inventory": inventory
#     }

# # =========================================================
# # PUT - Update Inventory
# # =========================================================

# @router.put("/{inventory_id}")
# def update_inventory(
#     inventory_id: str,
#     data: Inventory
# ):

#     inventory_collection = db["inventory"]
#     ingredients_collection = db["ingredients"]

#     # Check inventory ID
#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     # Check inventory exists
#     existing_inventory = inventory_collection.find_one(
#         {"_id": ObjectId(inventory_id)}
#     )

#     if not existing_inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     # Check ingredient ID
#     if not ObjectId.is_valid(data.ingredient_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid ingredient ID"
#         )

#     # Check ingredient exists
#     ingredient = ingredients_collection.find_one(
#         {"_id": ObjectId(data.ingredient_id)}
#     )

#     if not ingredient:
#         raise HTTPException(
#             status_code=404,
#             detail="Ingredient not found"
#         )

#     update_data = {
#         "ingredient_id": data.ingredient_id,
#         "ingredient_name": ingredient["name"],
#         "quantity": data.quantity,
#         "unit": data.unit,
#         "minimum_stock": data.minimum_stock,
#         "location": data.location
#     }

#     inventory_collection.update_one(
#         {"_id": ObjectId(inventory_id)},
#         {"$set": update_data}
#     )

#     return {
#         "status": "success",
#         "message": "Inventory updated successfully"
#     }


# # =========================================================
# # DELETE - Delete Inventory
# # =========================================================

# @router.delete("/{inventory_id}")
# def delete_inventory(inventory_id: str):

#     inventory_collection = db["inventory"]

#     # Check inventory ID
#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     result = inventory_collection.delete_one(
#         {"_id": ObjectId(inventory_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory deleted successfully"
#     }


# from fastapi import APIRouter, HTTPException
# from bson import ObjectId
# from app.models.inventory_model import InventoryCreate, InventoryUpdate
# from app.db_config import db


# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# # MongoDB collection
# inventory_collection = db["inventory"]


# # =========================================================
# # GET ALL INVENTORY
# # =========================================================

# @router.get("/")
# def get_inventory():

#     inventory = []

#     for item in inventory_collection.find():

#         item["_id"] = str(item["_id"])

#         inventory.append(item)

#     return {
#         "status": "success",
#         "count": len(inventory),
#         "inventory": inventory
#     }


# # =========================================================
# # POST - ADD INVENTORY
# # =========================================================

# @router.post("/")
# def add_inventory(inventory: InventoryCreate):

#     inventory_data = inventory.model_dump()

#     result = inventory_collection.insert_one(inventory_data)

#     return {
#         "status": "success",
#         "message": "Inventory added successfully",
#         "inventory_id": str(result.inserted_id)
#     }


# # =========================================================
# # PUT - UPDATE INVENTORY
# # =========================================================

# @router.put("/{inventory_id}")
# def update_inventory(
#     inventory_id: str,
#     inventory: InventoryUpdate
# ):

#     # Check valid MongoDB ObjectId
#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     # Remove fields that were not provided
#     update_data = {
#         key: value
#         for key, value in inventory.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = inventory_collection.update_one(
#         {"_id": ObjectId(inventory_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory updated successfully"
#     }


# # =========================================================
# # DELETE - DELETE INVENTORY
# # =========================================================

# @router.delete("/{inventory_id}")
# def delete_inventory(inventory_id: str):

#     # Check valid MongoDB ObjectId
#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     result = inventory_collection.delete_one(
#         {"_id": ObjectId(inventory_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory deleted successfully"
#     }


# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.inventory_model import (
#     InventoryCreate,
#     InventoryUpdate
# )


# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# inventory_collection = db["inventory"]


# # =====================================================
# # CREATE INVENTORY
# # =====================================================

# @router.post("/")
# def create_inventory(inventory: InventoryCreate):

#     existing = inventory_collection.find_one({
#         "ingredient_name": inventory.ingredient_name
#     })

#     if existing:
#         raise HTTPException(
#             status_code=400,
#             detail="Inventory item already exists"
#         )

#     inventory_data = inventory.model_dump()

#     result = inventory_collection.insert_one(
#         inventory_data
#     )

#     return {
#         "status": "success",
#         "message": "Inventory created successfully",
#         "inventory_id": str(result.inserted_id)
#     }


# # =====================================================
# # GET ALL INVENTORY
# # =====================================================

# @router.get("/")
# def get_all_inventory():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     for item in inventory_items:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(inventory_items),
#         "inventory": inventory_items
#     }


# # =====================================================
# # GET SINGLE INVENTORY
# # =====================================================

# @router.get("/{inventory_id}")
# def get_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     inventory = inventory_collection.find_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if not inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     inventory["_id"] = str(inventory["_id"])

#     return {
#         "status": "success",
#         "inventory": inventory
#     }


# # =====================================================
# # UPDATE INVENTORY
# # =====================================================

# @router.put("/{inventory_id}")
# def update_inventory(
#     inventory_id: str,
#     inventory: InventoryUpdate
# ):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     update_data = {
#         key: value
#         for key, value in inventory.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = inventory_collection.update_one(
#         {"_id": ObjectId(inventory_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory updated successfully"
#     }


# # =====================================================
# # DELETE INVENTORY
# # =====================================================

# @router.delete("/{inventory_id}")
# def delete_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     result = inventory_collection.delete_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory deleted successfully"
#     }   

# # =====================================================
# # GET LOW STOCK INVENTORY
# # =====================================================

# @router.get("/low-stock")
# def get_low_stock_inventory():

#     low_stock_items = list(
#         inventory_collection.find({
#             "$expr": {
#                 "$lte": [
#                     "$quantity",
#                     "$minimum_stock"
#                 ]
#             }
#         })
#     )

#     for item in low_stock_items:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(low_stock_items),
#         "low_stock": low_stock_items
#     }


# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.inventory_model import (
#     InventoryCreate,
#     InventoryUpdate
# )


# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# inventory_collection = db["inventory"]


# # =====================================================
# # CREATE INVENTORY
# # =====================================================

# @router.post("/")
# def create_inventory(inventory: InventoryCreate):

#     existing = inventory_collection.find_one({
#         "ingredient_name": inventory.ingredient_name
#     })

#     if existing:
#         raise HTTPException(
#             status_code=400,
#             detail="Inventory item already exists"
#         )

#     inventory_data = inventory.model_dump()

#     result = inventory_collection.insert_one(
#         inventory_data
#     )

#     return {
#         "status": "success",
#         "message": "Inventory created successfully",
#         "inventory_id": str(result.inserted_id)
#     }


# # =====================================================
# # GET ALL INVENTORY
# # =====================================================

# @router.get("/")
# def get_all_inventory():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     for item in inventory_items:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(inventory_items),
#         "inventory": inventory_items
#     }


# # =====================================================
# # GET LOW STOCK INVENTORY
# # =====================================================

# @router.get("/low-stock")
# def get_low_stock_inventory( ):

#     low_stock_items = list(
#         inventory_collection.find({
#             "$expr": {
#                 "$lte": [
#                     "$quantity",
#                     "$minimum_stock"
#                 ]
#             }
#         })
#     )

#     for item in low_stock_items:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(low_stock_items),
#         "low_stock": low_stock_items
#     }


# # =====================================================
# # GET SINGLE INVENTORY
# # =====================================================

# @router.get("/{inventory_id}")
# def get_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     inventory = inventory_collection.find_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if not inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     inventory["_id"] = str(inventory["_id"])

#     return {
#         "status": "success",
#         "inventory": inventory
#     }


# # =====================================================
# # UPDATE INVENTORY
# # =====================================================

# @router.put("/{inventory_id}")
# def update_inventory(
#     inventory_id: str,
#     inventory: InventoryUpdate
# ):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     update_data = {
#         key: value
#         for key, value in inventory.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = inventory_collection.update_one(
#         {"_id": ObjectId(inventory_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory updated successfully"
#     }


# # =====================================================
# # DELETE INVENTORY
# # =====================================================

# @router.delete("/{inventory_id}")
# def delete_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     result = inventory_collection.delete_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory deleted successfully"
#     }       

# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.inventory_model import (
#     InventoryCreate,
#     InventoryUpdate
# )


# router = APIRouter(
#     prefix="/inventory",
#     tags=["Inventory"]
# )


# inventory_collection = db["inventory"]
# suppliers_collection = db["suppliers"]


# # =====================================================
# # CREATE INVENTORY
# # =====================================================

# @router.post("/")
# def create_inventory(inventory: InventoryCreate):

#     # -------------------------------------------------
#     # Check if inventory already exists
#     # -------------------------------------------------

#     existing = inventory_collection.find_one({
#         "ingredient_name": inventory.ingredient_name
#     })

#     if existing:
#         raise HTTPException(
#             status_code=400,
#             detail="Inventory item already exists"
#         )

#     # -------------------------------------------------
#     # Check Supplier
#     # -------------------------------------------------

#     if inventory.supplier:

#         if not ObjectId.is_valid(inventory.supplier):
#             raise HTTPException(
#                 status_code=400,
#                 detail="Invalid supplier ID"
#             )

#         supplier = suppliers_collection.find_one({
#             "_id": ObjectId(inventory.supplier)
#         })

#         if not supplier:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Supplier not found"
#             )

#     # -------------------------------------------------
#     # Insert Inventory
#     # -------------------------------------------------

#     inventory_data = inventory.model_dump()

#     result = inventory_collection.insert_one(
#         inventory_data
#     )

#     return {
#         "status": "success",
#         "message": "Inventory created successfully",
#         "inventory_id": str(result.inserted_id)
#     }


# # =====================================================
# # GET ALL INVENTORY
# # =====================================================

# @router.get("/")
# def get_all_inventory():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     for item in inventory_items:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(inventory_items),
#         "inventory": inventory_items
#     }


# # =====================================================
# # GET LOW STOCK INVENTORY
# # =====================================================

# @router.get("/low-stock")
# def get_low_stock_inventory():

#     low_stock_items = list(
#         inventory_collection.find({
#             "$expr": {
#                 "$lte": [
#                     "$quantity",
#                     "$minimum_stock"
#                 ]
#             }
#         })
#     )

#     for item in low_stock_items:
#         item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "count": len(low_stock_items),
#         "low_stock": low_stock_items
#     }


# # =====================================================
# # GET INVENTORY WITH SUPPLIER
# # =====================================================

# @router.get("/{inventory_id}/supplier")
# def get_inventory_supplier(inventory_id: str):

#     # -------------------------------------------------
#     # Validate Inventory ID
#     # -------------------------------------------------

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     # -------------------------------------------------
#     # Find Inventory
#     # -------------------------------------------------

#     inventory = inventory_collection.find_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if not inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     # -------------------------------------------------
#     # Check Supplier ID
#     # -------------------------------------------------

#     supplier_id = inventory.get("supplier")

#     if not supplier_id:
#         raise HTTPException(
#             status_code=404,
#             detail="No supplier assigned to this inventory"
#         )

#     if not ObjectId.is_valid(supplier_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid supplier ID stored in inventory"
#         )

#     # -------------------------------------------------
#     # Find Supplier
#     # -------------------------------------------------

#     supplier = suppliers_collection.find_one({
#         "_id": ObjectId(supplier_id)
#     })

#     if not supplier:
#         raise HTTPException(
#             status_code=404,
#             detail="Supplier not found"
#         )

#     # Convert ObjectIds to strings
#     inventory["_id"] = str(inventory["_id"])
#     supplier["_id"] = str(supplier["_id"])

#     return {
#         "status": "success",
#         "inventory": inventory,
#         "supplier": supplier
#     }


# # =====================================================
# # GET SINGLE INVENTORY
# # =====================================================

# @router.get("/{inventory_id}")
# def get_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     inventory = inventory_collection.find_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if not inventory:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     inventory["_id"] = str(inventory["_id"])

#     return {
#         "status": "success",
#         "inventory": inventory
#     }


# # =====================================================
# # UPDATE INVENTORY
# # =====================================================

# @router.put("/{inventory_id}")
# def update_inventory(
#     inventory_id: str,
#     inventory: InventoryUpdate
# ):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     # -------------------------------------------------
#     # Check Supplier if supplied during update
#     # -------------------------------------------------

#     if inventory.supplier is not None:

#         if not ObjectId.is_valid(inventory.supplier):
#             raise HTTPException(
#                 status_code=400,
#                 detail="Invalid supplier ID"
#             )

#         supplier = suppliers_collection.find_one({
#             "_id": ObjectId(inventory.supplier)
#         })

#         if not supplier:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Supplier not found"
#             )

#     # -------------------------------------------------
#     # Prepare Update
#     # -------------------------------------------------

#     update_data = {
#         key: value
#         for key, value in inventory.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = inventory_collection.update_one(
#         {"_id": ObjectId(inventory_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory updated successfully"
#     }


# # =====================================================
# # DELETE INVENTORY
# # =====================================================

# @router.delete("/{inventory_id}")
# def delete_inventory(inventory_id: str):

#     if not ObjectId.is_valid(inventory_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid inventory ID"
#         )

#     result = inventory_collection.delete_one({
#         "_id": ObjectId(inventory_id)
#     })

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Inventory not found"
#         )

#     return {
#         "status": "success",
#         "message": "Inventory deleted successfully"
#     }


from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.db_config import db
from app.models.inventory_model import (
    InventoryCreate,
    InventoryUpdate
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

inventory_collection = db["inventory"]
suppliers_collection = db["suppliers"]


# =========================================================
# CREATE INVENTORY
# =========================================================

@router.post("/")
async def create_inventory(inventory: InventoryCreate):

    # -----------------------------------------------------
    # Check duplicate ingredient
    # -----------------------------------------------------
    existing = inventory_collection.find_one({
        "ingredient_name": inventory.ingredient_name
    })

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Inventory item already exists"
        )

    # -----------------------------------------------------
    # Check supplier
    # -----------------------------------------------------
    if inventory.supplier_id:

        if not ObjectId.is_valid(inventory.supplier_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid supplier ID"
            )

        supplier = suppliers_collection.find_one({
            "_id": ObjectId(inventory.supplier_id)
        })

        if not supplier:
            raise HTTPException(
                status_code=404,
                detail="Supplier not found"
            )

    # -----------------------------------------------------
    # Create inventory
    # -----------------------------------------------------
    inventory_data = inventory.model_dump()

    result = inventory_collection.insert_one(
        inventory_data
    )

    return {
        "status": "success",
        "message": "Inventory created successfully",
        "inventory_id": str(result.inserted_id)
    }


# =========================================================
# GET ALL INVENTORY
# =========================================================

@router.get("/")
async def get_all_inventory():

    inventory_items = list(
        inventory_collection.find()
    )

    for item in inventory_items:
        item["_id"] = str(item["_id"])

    return {
        "status": "success",
        "count": len(inventory_items),
        "inventory": inventory_items
    }


# =========================================================
# GET LOW STOCK
# =========================================================

@router.get("/low-stock")
async def get_low_stock_inventory():

    low_stock_items = list(
        inventory_collection.find({
            "$expr": {
                "$lte": [
                    "$quantity",
                    "$minimum_stock"
                ]
            }
        })
    )

    for item in low_stock_items:
        item["_id"] = str(item["_id"])

    return {
        "status": "success",
        "count": len(low_stock_items),
        "low_stock": low_stock_items
    }


# =========================================================
# GET INVENTORY BY ID
# =========================================================

@router.get("/{inventory_id}")
async def get_inventory(inventory_id: str):

    if not ObjectId.is_valid(inventory_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid inventory ID"
        )

    inventory = inventory_collection.find_one({
        "_id": ObjectId(inventory_id)
    })

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    inventory["_id"] = str(inventory["_id"])

    return {
        "status": "success",
        "inventory": inventory
    }


# =========================================================
# UPDATE INVENTORY
# =========================================================

@router.put("/{inventory_id}")
async def update_inventory(
    inventory_id: str,
    inventory: InventoryUpdate
):

    if not ObjectId.is_valid(inventory_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid inventory ID"
        )

    # -----------------------------------------------------
    # Check supplier if being changed
    # -----------------------------------------------------
    if inventory.supplier_id:

        if not ObjectId.is_valid(inventory.supplier_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid supplier ID"
            )

        supplier = suppliers_collection.find_one({
            "_id": ObjectId(inventory.supplier_id)
        })

        if not supplier:
            raise HTTPException(
                status_code=404,
                detail="Supplier not found"
            )

    update_data = {
        key: value
        for key, value in inventory.model_dump().items()
        if value is not None
    }

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    result = inventory_collection.update_one(
        {"_id": ObjectId(inventory_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    return {
        "status": "success",
        "message": "Inventory updated successfully"
    }


# =========================================================
# DELETE INVENTORY
# =========================================================

@router.delete("/{inventory_id}")
async def delete_inventory(inventory_id: str):

    if not ObjectId.is_valid(inventory_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid inventory ID"
        )

    result = inventory_collection.delete_one({
        "_id": ObjectId(inventory_id)
    })

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    return {
        "status": "success",
        "message": "Inventory deleted successfully"
    }