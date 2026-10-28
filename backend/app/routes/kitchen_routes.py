# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.kitchen_model import (
#     KitchenCreate,
#     KitchenUpdate
# )

# router = APIRouter(
#     prefix="/kitchen",
#     tags=["Kitchen"]
# )

# kitchen_collection = db["kitchen_orders"]


# # =========================================================
# # CREATE KITCHEN ORDER
# # =========================================================
# @router.post("/")
# async def create_kitchen_order(order: KitchenCreate):

#     order_data = order.model_dump()

#     result = kitchen_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Kitchen order created successfully",
#         "kitchen_order_id": str(result.inserted_id)
#     }


# # =========================================================
# # GET ALL KITCHEN ORDERS
# # =========================================================
# @router.get("/")
# async def get_kitchen_orders():

#     orders = []

#     for order in kitchen_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "kitchen_orders": orders
#     }


# # =========================================================
# # GET KITCHEN ORDER BY ID
# # =========================================================
# @router.get("/{kitchen_order_id}")
# async def get_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "kitchen_order": order
#     }


# # =========================================================
# # UPDATE KITCHEN ORDER
# # =========================================================
# @router.put("/{kitchen_order_id}")
# async def update_kitchen_order(
#     kitchen_order_id: str,
#     order: KitchenUpdate
# ):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     update_data = {
#         key: value
#         for key, value in order.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order updated successfully"
#     }


# # =========================================================
# # DELETE KITCHEN ORDER
# # =========================================================
# @router.delete("/{kitchen_order_id}")
# async def delete_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     result = kitchen_collection.delete_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order deleted successfully"
#     }


# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.kitchen_model import (
#     KitchenCreate,
#     KitchenUpdate
# )

# router = APIRouter(
#     prefix="/kitchen",
#     tags=["Kitchen"]
# )

# kitchen_collection = db["kitchen_orders"]
# inventory_collection = db["inventory"]


# # =========================================================
# # CREATE KITCHEN ORDER
# # =========================================================
# @router.post("/")
# async def create_kitchen_order(order: KitchenCreate):

#     order_data = order.model_dump()

#     result = kitchen_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Kitchen order created successfully",
#         "kitchen_order_id": str(result.inserted_id)
#     }


# # =========================================================
# # GET ALL KITCHEN ORDERS
# # =========================================================
# @router.get("/")
# async def get_kitchen_orders():

#     orders = []

#     for order in kitchen_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "kitchen_orders": orders
#     }


# # =========================================================
# # GET KITCHEN ORDER BY ID
# # =========================================================
# @router.get("/{kitchen_order_id}")
# async def get_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "kitchen_order": order
#     }


# # =========================================================
# # UPDATE KITCHEN ORDER
# # =========================================================
# @router.put("/{kitchen_order_id}")
# async def update_kitchen_order(
#     kitchen_order_id: str,
#     order: KitchenUpdate
# ):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     update_data = {
#         key: value
#         for key, value in order.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order updated successfully"
#     }


# # =========================================================
# # DELETE KITCHEN ORDER
# # =========================================================
# @router.delete("/{kitchen_order_id}")
# async def delete_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     result = kitchen_collection.delete_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order deleted successfully"
#     }


# # =========================================================
# # START KITCHEN ORDER
# # =========================================================
# @router.post("/{kitchen_order_id}/start")
# async def start_kitchen_order(kitchen_order_id: str):

#     # -----------------------------------------
#     # Check Kitchen Order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     # -----------------------------------------
#     # Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # Check current status
#     # -----------------------------------------
#     if order.get("status") != "pending":
#         raise HTTPException(
#             status_code=400,
#             detail=f"Kitchen order cannot be started because its status is '{order.get('status')}'"
#         )

#     # -----------------------------------------
#     # Get required ingredients
#     # -----------------------------------------
#     ingredients = order.get("ingredients", [])

#     if not ingredients:
#         raise HTTPException(
#             status_code=400,
#             detail="No ingredients specified for this kitchen order"
#         )

#     insufficient_stock = []

#     # -----------------------------------------
#     # Check every ingredient
#     # -----------------------------------------
#     for ingredient in ingredients:

#         ingredient_name = ingredient.get("ingredient_name")
#         quantity_required = ingredient.get("quantity_required", 0)
#         unit = ingredient.get("unit")

#         inventory = inventory_collection.find_one(
#             {
#                 "ingredient_name": ingredient_name
#             }
#         )

#         # Ingredient not found in inventory
#         if not inventory:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": 0,
#                 "unit": unit,
#                 "message": "Ingredient not found in inventory"
#             })

#             continue

#         available_quantity = inventory.get("quantity", 0)

#         # Not enough stock
#         if available_quantity < quantity_required:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": available_quantity,
#                 "unit": unit,
#                 "message": "Insufficient stock"
#             })

#     # -----------------------------------------
#     # If stock is insufficient
#     # -----------------------------------------
#     if insufficient_stock:

#         return {
#             "status": "failed",
#             "message": "Insufficient inventory to start kitchen order",
#             "kitchen_order_id": kitchen_order_id,
#             "insufficient_stock": insufficient_stock
#         }

#     # -----------------------------------------
#     # All ingredients available
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "preparing"
#             }
#         }
#     )

#     return {
#         "status": "success",
#         "message": "Kitchen order started successfully",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "preparing"
#     }



# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.kitchen_model import (
#     KitchenCreate,
#     KitchenUpdate
# )

# router = APIRouter(
#     prefix="/kitchen",
#     tags=["Kitchen"]
# )

# kitchen_collection = db["kitchen_orders"]
# inventory_collection = db["inventory"]


# # =========================================================
# # CREATE KITCHEN ORDER
# # =========================================================
# @router.post("/")
# async def create_kitchen_order(order: KitchenCreate):

#     order_data = order.model_dump()

#     result = kitchen_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Kitchen order created successfully",
#         "kitchen_order_id": str(result.inserted_id)
#     }


# # =========================================================
# # GET ALL KITCHEN ORDERS
# # =========================================================
# @router.get("/")
# async def get_kitchen_orders():

#     orders = []

#     for order in kitchen_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "kitchen_orders": orders
#     }


# # =========================================================
# # GET KITCHEN ORDER BY ID
# # =========================================================
# @router.get("/{kitchen_order_id}")
# async def get_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "kitchen_order": order
#     }


# # =========================================================
# # UPDATE KITCHEN ORDER
# # =========================================================
# @router.put("/{kitchen_order_id}")
# async def update_kitchen_order(
#     kitchen_order_id: str,
#     order: KitchenUpdate
# ):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     update_data = {
#         key: value
#         for key, value in order.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order updated successfully"
#     }


# # =========================================================
# # DELETE KITCHEN ORDER
# # =========================================================
# @router.delete("/{kitchen_order_id}")
# async def delete_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     result = kitchen_collection.delete_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order deleted successfully"
#     }


# # =========================================================
# # START KITCHEN ORDER
# # CHECK INVENTORY + USE INGREDIENTS
# # =========================================================
# # @router.post("/{kitchen_order_id}/start")
# # async def start_kitchen_order(kitchen_order_id: str):

# #     # -----------------------------------------
# #     # 1. Validate Kitchen Order ID
# #     # -----------------------------------------
# #     if not ObjectId.is_valid(kitchen_order_id):
# #         raise HTTPException(
# #             status_code=400,
# #             detail="Invalid kitchen order ID"
# #         )

#     # -----------------------------------------
#     # 2. Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # 3. Check current status
#     # -----------------------------------------
#     if order.get("status") != "pending":
#         raise HTTPException(
#             status_code=400,
#             detail=(
#                 f"Kitchen order cannot be started "
#                 f"because its status is '{order.get('status')}'"
#             )
#         )

#     # -----------------------------------------
#     # 4. Get required ingredients
#     # -----------------------------------------
#     ingredients = order.get("ingredients", [])

#     if not ingredients:
#         raise HTTPException(
#             status_code=400,
#             detail="No ingredients specified for this kitchen order"
#         )

#     insufficient_stock = []
#     available_inventory = []

#     # -----------------------------------------
#     # 5. Check ALL ingredients first
#     # -----------------------------------------
#     for ingredient in ingredients:

#         ingredient_name = ingredient.get("ingredient_name")
#         quantity_required = ingredient.get(
#             "quantity_required",
#             0
#         )
#         unit = ingredient.get("unit")

#         inventory = inventory_collection.find_one(
#             {
#                 "ingredient_name": ingredient_name
#             }
#         )

#         # Ingredient does not exist
#         if not inventory:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": 0,
#                 "unit": unit,
#                 "message": "Ingredient not found in inventory"
#             })

#             continue

#         available_quantity = inventory.get(
#             "quantity",
#             0
#         )

#         # Not enough stock
#         if available_quantity < quantity_required:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": available_quantity,
#                 "unit": unit,
#                 "message": "Insufficient stock"
#             })

#         else:

#             available_inventory.append({
#                 "ingredient_name": ingredient_name,
#                 "quantity_required": quantity_required,
#                 "unit": unit,
#                 "inventory_id": inventory["_id"]
#             })

#     # -----------------------------------------
#     # 6. Stop if ANY ingredient is insufficient
#     # -----------------------------------------
#     if insufficient_stock:

#         return {
#             "status": "failed",
#             "message": "Insufficient inventory to start kitchen order",
#             "kitchen_order_id": kitchen_order_id,
#             "insufficient_stock": insufficient_stock
#         }

#     # -----------------------------------------
#     # 7. Subtract ingredients from inventory
#     # -----------------------------------------
#     used_ingredients = []

#     for item in available_inventory:

#         inventory_id = item["inventory_id"]
#         quantity_required = item["quantity_required"]

#         inventory = inventory_collection.find_one(
#             {"_id": inventory_id}
#         )

#         old_quantity = inventory.get(
#             "quantity",
#             0
#         )

#         new_quantity = (
#             old_quantity - quantity_required
#         )

#         inventory_collection.update_one(
#             {"_id": inventory_id},
#             {
#                 "$set": {
#                     "quantity": new_quantity
#                 }
#             }
#         )

#         used_ingredients.append({
#             "ingredient_name": item["ingredient_name"],
#             "used_quantity": quantity_required,
#             "remaining_quantity": new_quantity,
#             "unit": item["unit"]
#         })

#     # -----------------------------------------
#     # 8. Change Kitchen status
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "preparing"
#             }
#         }
#     )

#     # -----------------------------------------
#     # 9. Success response
#     # -----------------------------------------
#     return {
#         "status": "success",
#         "message": "Kitchen order started successfully",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "preparing",
#         "used_ingredients": used_ingredients
#     }



# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.kitchen_model import (
#     KitchenCreate,
#     KitchenUpdate
# )

# router = APIRouter(
#     prefix="/kitchen",
#     tags=["Kitchen"]
# )

# kitchen_collection = db["kitchen_orders"]
# inventory_collection = db["inventory"]


# # =========================================================
# # CREATE KITCHEN ORDER
# # =========================================================
# @router.post("/")
# async def create_kitchen_order(order: KitchenCreate):

#     order_data = order.model_dump()

#     result = kitchen_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Kitchen order created successfully",
#         "kitchen_order_id": str(result.inserted_id)
#     }


# # =========================================================
# # GET ALL KITCHEN ORDERS
# # =========================================================
# @router.get("/")
# async def get_kitchen_orders():

#     orders = []

#     for order in kitchen_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "kitchen_orders": orders
#     }


# # =========================================================
# # GET KITCHEN ORDER BY ID
# # =========================================================
# @router.get("/{kitchen_order_id}")
# async def get_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "kitchen_order": order
#     }


# # =========================================================
# # UPDATE KITCHEN ORDER
# # =========================================================
# @router.put("/{kitchen_order_id}")
# async def update_kitchen_order(
#     kitchen_order_id: str,
#     order: KitchenUpdate
# ):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     update_data = {
#         key: value
#         for key, value in order.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order updated successfully"
#     }


# # =========================================================
# # DELETE KITCHEN ORDER
# # =========================================================
# @router.delete("/{kitchen_order_id}")
# async def delete_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     result = kitchen_collection.delete_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order deleted successfully"
#     }


# # =========================================================
# # START KITCHEN ORDER
# # CHECK INVENTORY + DEDUCT INGREDIENTS
# # =========================================================
# @router.post("/{kitchen_order_id}/start")
# async def start_kitchen_order(kitchen_order_id: str):

#     # -----------------------------------------
#     # 1. Validate Kitchen Order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     # -----------------------------------------
#     # 2. Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # 3. Check current status
#     # -----------------------------------------
#     if order.get("status") != "pending":
#         raise HTTPException(
#             status_code=400,
#             detail=(
#                 f"Kitchen order cannot be started "
#                 f"because its status is '{order.get('status')}'"
#             )
#         )

#     # -----------------------------------------
#     # 4. Get required ingredients
#     # -----------------------------------------
#     ingredients = order.get("ingredients", [])

#     if not ingredients:
#         raise HTTPException(
#             status_code=400,
#             detail="No ingredients specified for this kitchen order"
#         )

#     insufficient_stock = []
#     available_inventory = []

#     # -----------------------------------------
#     # 5. Check ALL ingredients
#     # -----------------------------------------
#     for ingredient in ingredients:

#         ingredient_name = ingredient.get("ingredient_name")
#         quantity_required = ingredient.get(
#             "quantity_required",
#             0
#         )
#         unit = ingredient.get("unit")

#         inventory = inventory_collection.find_one({
#             "ingredient_name": ingredient_name
#         })

#         # Ingredient not found
#         if not inventory:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": 0,
#                 "unit": unit,
#                 "message": "Ingredient not found in inventory"
#             })

#             continue

#         available_quantity = inventory.get(
#             "quantity",
#             0
#         )

#         # Not enough stock
#         if available_quantity < quantity_required:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": available_quantity,
#                 "unit": unit,
#                 "message": "Insufficient stock"
#             })

#         else:

#             available_inventory.append({
#                 "ingredient_name": ingredient_name,
#                 "quantity_required": quantity_required,
#                 "unit": unit,
#                 "inventory_id": inventory["_id"]
#             })

#     # -----------------------------------------
#     # 6. Stop if stock is insufficient
#     # -----------------------------------------
#     if insufficient_stock:

#         return {
#             "status": "failed",
#             "message": "Insufficient inventory to start kitchen order",
#             "kitchen_order_id": kitchen_order_id,
#             "insufficient_stock": insufficient_stock
#         }

#     # -----------------------------------------
#     # 7. Deduct ingredients from inventory
#     # -----------------------------------------
#     used_ingredients = []

#     for item in available_inventory:

#         inventory_id = item["inventory_id"]
#         quantity_required = item["quantity_required"]

#         inventory = inventory_collection.find_one({
#             "_id": inventory_id
#         })

#         old_quantity = inventory.get(
#             "quantity",
#             0
#         )

#         new_quantity = (
#             old_quantity - quantity_required
#         )

#         inventory_collection.update_one(
#             {"_id": inventory_id},
#             {
#                 "$set": {
#                     "quantity": new_quantity
#                 }
#             }
#         )

#         used_ingredients.append({
#             "ingredient_name": item["ingredient_name"],
#             "used_quantity": quantity_required,
#             "previous_quantity": old_quantity,
#             "remaining_quantity": new_quantity,
#             "unit": item["unit"]
#         })

#     # -----------------------------------------
#     # 8. Change kitchen status
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "preparing"
#             }
#         }
#     )

#     # -----------------------------------------
#     # 9. Success response
#     # -----------------------------------------
#     return {
#         "status": "success",
#         "message": "Kitchen order started successfully",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "preparing",
#         "used_ingredients": used_ingredients
#     }

# # =========================================================
# # MARK KITCHEN ORDER AS READY
# # =========================================================
# @router.post("/{kitchen_order_id}/ready")
# async def mark_kitchen_order_ready(kitchen_order_id: str):

#     # -----------------------------------------
#     # 1. Validate Kitchen Order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     # -----------------------------------------
#     # 2. Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # 3. Check current status
#     # -----------------------------------------
#     if order.get("status") != "preparing":
#         raise HTTPException(
#             status_code=400,
#             detail=(
#                 f"Kitchen order cannot be marked ready "
#                 f"because its status is '{order.get('status')}'"
#             )
#         )

#     # -----------------------------------------
#     # 4. Change status to ready
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "ready"
#             }
#         }
#     )

#     # -----------------------------------------
#     # 5. Response
#     # -----------------------------------------
#     return {
#         "status": "success",
#         "message": "Kitchen order is ready",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "ready"
#     }

# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.kitchen_model import (
#     KitchenCreate,
#     KitchenUpdate
# )

# router = APIRouter(
#     prefix="/kitchen",
#     tags=["Kitchen"]
# )

# kitchen_collection = db["kitchen_orders"]
# inventory_collection = db["inventory"]


# # =========================================================
# # CREATE KITCHEN ORDER
# # =========================================================
# @router.post("/")
# async def create_kitchen_order(order: KitchenCreate):

#     order_data = order.model_dump()

#     result = kitchen_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Kitchen order created successfully",
#         "kitchen_order_id": str(result.inserted_id)
#     }


# # =========================================================
# # GET ALL KITCHEN ORDERS
# # =========================================================
# @router.get("/")
# async def get_kitchen_orders():

#     orders = []

#     for order in kitchen_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "kitchen_orders": orders
#     }


# # =========================================================
# # GET KITCHEN ORDER BY ID
# # =========================================================
# @router.get("/{kitchen_order_id}")
# async def get_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "kitchen_order": order
#     }


# # =========================================================
# # UPDATE KITCHEN ORDER
# # =========================================================
# @router.put("/{kitchen_order_id}")
# async def update_kitchen_order(
#     kitchen_order_id: str,
#     order: KitchenUpdate
# ):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     update_data = {
#         key: value
#         for key, value in order.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order updated successfully"
#     }


# # =========================================================
# # DELETE KITCHEN ORDER
# # =========================================================
# @router.delete("/{kitchen_order_id}")
# async def delete_kitchen_order(kitchen_order_id: str):

#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     result = kitchen_collection.delete_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Kitchen order deleted successfully"
#     }


# # =========================================================
# # START KITCHEN ORDER
# # CHECK INVENTORY + DEDUCT INGREDIENTS
# # =========================================================
# @router.post("/{kitchen_order_id}/start")
# async def start_kitchen_order(kitchen_order_id: str):

#     # -----------------------------------------
#     # 1. Validate Kitchen Order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     # -----------------------------------------
#     # 2. Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # 3. Check current status
#     # -----------------------------------------
#     if order.get("status") != "pending":
#         raise HTTPException(
#             status_code=400,
#             detail=(
#                 f"Kitchen order cannot be started "
#                 f"because its status is '{order.get('status')}'"
#             )
#         )

#     # -----------------------------------------
#     # 4. Get required ingredients
#     # -----------------------------------------
#     ingredients = order.get("ingredients", [])

#     if not ingredients:
#         raise HTTPException(
#             status_code=400,
#             detail="No ingredients specified for this kitchen order"
#         )

#     insufficient_stock = []
#     available_inventory = []

#     # -----------------------------------------
#     # 5. Check ALL ingredients
#     # -----------------------------------------
#     for ingredient in ingredients:

#         ingredient_name = ingredient.get("ingredient_name")

#         quantity_required = ingredient.get(
#             "quantity_required",
#             0
#         )

#         unit = ingredient.get("unit")

#         inventory = inventory_collection.find_one({
#             "ingredient_name": ingredient_name
#         })

#         # Ingredient not found
#         if not inventory:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": 0,
#                 "unit": unit,
#                 "message": "Ingredient not found in inventory"
#             })

#             continue

#         available_quantity = inventory.get(
#             "quantity",
#             0
#         )

#         # Not enough stock
#         if available_quantity < quantity_required:

#             insufficient_stock.append({
#                 "ingredient_name": ingredient_name,
#                 "required": quantity_required,
#                 "available": available_quantity,
#                 "unit": unit,
#                 "message": "Insufficient stock"
#             })

#         else:

#             available_inventory.append({
#                 "ingredient_name": ingredient_name,
#                 "quantity_required": quantity_required,
#                 "unit": unit,
#                 "inventory_id": inventory["_id"]
#             })

#     # -----------------------------------------
#     # 6. Stop if stock is insufficient
#     # -----------------------------------------
#     if insufficient_stock:

#         return {
#             "status": "failed",
#             "message": "Insufficient inventory to start kitchen order",
#             "kitchen_order_id": kitchen_order_id,
#             "insufficient_stock": insufficient_stock
#         }

#     # -----------------------------------------
#     # 7. Deduct ingredients from inventory
#     # -----------------------------------------
#     used_ingredients = []

#     for item in available_inventory:

#         inventory_id = item["inventory_id"]

#         quantity_required = item["quantity_required"]

#         inventory = inventory_collection.find_one({
#             "_id": inventory_id
#         })

#         old_quantity = inventory.get(
#             "quantity",
#             0
#         )

#         new_quantity = (
#             old_quantity - quantity_required
#         )

#         inventory_collection.update_one(
#             {"_id": inventory_id},
#             {
#                 "$set": {
#                     "quantity": new_quantity
#                 }
#             }
#         )

#         used_ingredients.append({
#             "ingredient_name": item["ingredient_name"],
#             "used_quantity": quantity_required,
#             "previous_quantity": old_quantity,
#             "remaining_quantity": new_quantity,
#             "unit": item["unit"]
#         })

#     # -----------------------------------------
#     # 8. Change kitchen status
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "preparing"
#             }
#         }
#     )

#     # -----------------------------------------
#     # 9. Success response
#     # -----------------------------------------
#     return {
#         "status": "success",
#         "message": "Kitchen order started successfully",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "preparing",
#         "used_ingredients": used_ingredients
#     }


# # =========================================================
# # MARK KITCHEN ORDER AS READY
# # =========================================================
# @router.post("/{kitchen_order_id}/ready")
# async def mark_kitchen_order_ready(kitchen_order_id: str):

#     # -----------------------------------------
#     # 1. Validate Kitchen Order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     # -----------------------------------------
#     # 2. Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # 3. Check current status
#     # -----------------------------------------
#     if order.get("status") != "preparing":
#         raise HTTPException(
#             status_code=400,
#             detail=(
#                 f"Kitchen order cannot be marked ready "
#                 f"because its status is '{order.get('status')}'"
#             )
#         )

#     # -----------------------------------------
#     # 4. Change status to ready
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "ready"
#             }
#         }
#     )

#     # -----------------------------------------
#     # 5. Success response
#     # -----------------------------------------
#     return {
#         "status": "success",
#         "message": "Kitchen order is ready",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "ready"
#     }


# # =========================================================
# # MARK KITCHEN ORDER AS COMPLETED
# # =========================================================
# @router.post("/{kitchen_order_id}/complete")
# async def complete_kitchen_order(kitchen_order_id: str):

#     # -----------------------------------------
#     # 1. Validate Kitchen Order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(kitchen_order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid kitchen order ID"
#         )

#     # -----------------------------------------
#     # 2. Find Kitchen Order
#     # -----------------------------------------
#     order = kitchen_collection.find_one(
#         {"_id": ObjectId(kitchen_order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Kitchen order not found"
#         )

#     # -----------------------------------------
#     # 3. Check current status
#     # -----------------------------------------
#     if order.get("status") != "ready":
#         raise HTTPException(
#             status_code=400,
#             detail=(
#                 f"Kitchen order cannot be completed "
#                 f"because its status is '{order.get('status')}'"
#             )
#         )

#     # -----------------------------------------
#     # 4. Change status to completed
#     # -----------------------------------------
#     kitchen_collection.update_one(
#         {"_id": ObjectId(kitchen_order_id)},
#         {
#             "$set": {
#                 "status": "completed"
#             }
#         }
#     )

#     # -----------------------------------------
#     # 5. Success response
#     # -----------------------------------------
#     return {
#         "status": "success",
#         "message": "Kitchen order completed successfully",
#         "kitchen_order_id": kitchen_order_id,
#         "kitchen_status": "completed"
#     }
from fastapi import APIRouter, HTTPException
from bson import ObjectId
import re

from app.db_config import db
from app.models.kitchen_model import (
    KitchenCreate,
    KitchenUpdate
)

router = APIRouter(
    prefix="/kitchen",
    tags=["Kitchen"]
)

kitchen_collection = db["kitchen_orders"]
inventory_collection = db["inventory"]


# CREATE KITCHEN ORDER
@router.post("/")
async def create_kitchen_order(order: KitchenCreate):

    order_data = order.model_dump()

    result = kitchen_collection.insert_one(order_data)

    return {
        "status": "success",
        "message": "Kitchen order created successfully",
        "kitchen_order_id": str(result.inserted_id)
    }


# GET ALL KITCHEN ORDERS
@router.get("/")
async def get_kitchen_orders():

    orders = []

    for order in kitchen_collection.find():

        order["_id"] = str(order["_id"])

        orders.append(order)

    return {
        "status": "success",
        "count": len(orders),
        "kitchen_orders": orders
    }


# GET SINGLE KITCHEN ORDER
@router.get("/{kitchen_order_id}")
async def get_kitchen_order(kitchen_order_id: str):

    if not ObjectId.is_valid(kitchen_order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid kitchen order ID"
        )

    order = kitchen_collection.find_one(
        {"_id": ObjectId(kitchen_order_id)}
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Kitchen order not found"
        )

    order["_id"] = str(order["_id"])

    return {
        "status": "success",
        "kitchen_order": order
    }


# UPDATE KITCHEN ORDER
@router.put("/{kitchen_order_id}")
async def update_kitchen_order(
    kitchen_order_id: str,
    order: KitchenUpdate
):

    if not ObjectId.is_valid(kitchen_order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid kitchen order ID"
        )

    update_data = {
        key: value
        for key, value in order.model_dump().items()
        if value is not None
    }

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    result = kitchen_collection.update_one(
        {"_id": ObjectId(kitchen_order_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Kitchen order not found"
        )

    return {
        "status": "success",
        "message": "Kitchen order updated successfully"
    }


# DELETE KITCHEN ORDER
@router.delete("/{kitchen_order_id}")
async def delete_kitchen_order(kitchen_order_id: str):

    if not ObjectId.is_valid(kitchen_order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid kitchen order ID"
        )

    result = kitchen_collection.delete_one(
        {"_id": ObjectId(kitchen_order_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Kitchen order not found"
        )

    return {
        "status": "success",
        "message": "Kitchen order deleted successfully"
    }


# START KITCHEN ORDER
# CHECK INVENTORY + DEDUCT INGREDIENTS
@router.post("/{kitchen_order_id}/start")
async def start_kitchen_order(kitchen_order_id: str):

    if not ObjectId.is_valid(kitchen_order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid kitchen order ID"
        )

    # Find kitchen order
    kitchen_order = kitchen_collection.find_one(
        {"_id": ObjectId(kitchen_order_id)}
    )

    if not kitchen_order:
        raise HTTPException(
            status_code=404,
            detail="Kitchen order not found"
        )

    # Check current status
    current_status = kitchen_order.get(
        "status",
        "pending"
    ).lower()

    if current_status == "preparing":
        raise HTTPException(
            status_code=400,
            detail="Kitchen order is already being prepared"
        )

    if current_status == "ready":
        raise HTTPException(
            status_code=400,
            detail="Kitchen order is already ready"
        )

    # Get ingredients
    ingredients = kitchen_order.get(
        "ingredients",
        []
    )

    if not ingredients:
        raise HTTPException(
            status_code=400,
            detail="No ingredients found in kitchen order"
        )

    # ------------------------------------------------
    # STEP 1: CHECK ALL INGREDIENTS FIRST
    # ------------------------------------------------

    insufficient_items = []

    for ingredient in ingredients:

        ingredient_name = ingredient.get(
            "ingredient_name"
        )

        required_quantity = ingredient.get(
            "quantity_required",
            0
        )

        required_unit = ingredient.get(
            "unit",
            ""
        )

        inventory_item = inventory_collection.find_one(
            {
                "ingredient_name": {
                    "$regex": f"^{re.escape(ingredient_name)}$",
                    "$options": "i"
                }
            }
        )

        # Ingredient doesn't exist
        if not inventory_item:

            insufficient_items.append({
                "ingredient_name": ingredient_name,
                "required_quantity": required_quantity,
                "available_quantity": 0,
                "unit": required_unit,
                "reason": "Ingredient not found in inventory"
            })

            continue

        available_quantity = inventory_item.get(
            "quantity",
            0
        )

        inventory_unit = inventory_item.get(
            "unit",
            ""
        )

        # Check unit
        if inventory_unit.lower() != required_unit.lower():

            insufficient_items.append({
                "ingredient_name": ingredient_name,
                "required_quantity": required_quantity,
                "available_quantity": available_quantity,
                "required_unit": required_unit,
                "inventory_unit": inventory_unit,
                "reason": "Unit mismatch"
            })

            continue

        # Check quantity
        if available_quantity < required_quantity:

            insufficient_items.append({
                "ingredient_name": ingredient_name,
                "required_quantity": required_quantity,
                "available_quantity": available_quantity,
                "unit": required_unit,
                "reason": "Insufficient stock"
            })

    # ------------------------------------------------
    # STOP IF ANY INGREDIENT IS INSUFFICIENT
    # ------------------------------------------------

    if insufficient_items:

        return {
            "status": "insufficient_items",
            "message": "Kitchen order cannot be started",
            "kitchen_order_id": kitchen_order_id,
            "insufficient_items": insufficient_items
        }

    # ------------------------------------------------
    # STEP 2: DEDUCT INGREDIENTS FROM INVENTORY
    # ------------------------------------------------

    deducted_items = []

    for ingredient in ingredients:

        ingredient_name = ingredient.get(
            "ingredient_name"
        )

        required_quantity = ingredient.get(
            "quantity_required",
            0
        )

        required_unit = ingredient.get(
            "unit",
            ""
        )

        inventory_item = inventory_collection.find_one(
            {
                "ingredient_name": {
                    "$regex": f"^{re.escape(ingredient_name)}$",
                    "$options": "i"
                }
            }
        )

        old_quantity = inventory_item.get(
            "quantity",
            0
        )

        new_quantity = old_quantity - required_quantity

        inventory_collection.update_one(
            {
                "_id": inventory_item["_id"]
            },
            {
                "$set": {
                    "quantity": new_quantity
                }
            }
        )

        deducted_items.append({
            "ingredient_name": inventory_item.get(
                "ingredient_name"
            ),
            "used_quantity": required_quantity,
            "previous_stock": old_quantity,
            "remaining_stock": new_quantity,
            "unit": required_unit
        })

    # ------------------------------------------------
    # STEP 3: CHANGE KITCHEN STATUS
    # ------------------------------------------------

    kitchen_collection.update_one(
        {
            "_id": ObjectId(kitchen_order_id)
        },
        {
            "$set": {
                "status": "preparing"
            }
        }
    )

    return {
        "status": "success",
        "message": "Kitchen order started and ingredients deducted successfully",
        "kitchen_order_id": kitchen_order_id,
        "order_status": "preparing",
        "deducted_items": deducted_items
    }

# MARK KITCHEN ORDER AS READY
@router.post("/{kitchen_order_id}/ready")
async def mark_kitchen_order_ready(kitchen_order_id: str):

    if not ObjectId.is_valid(kitchen_order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid kitchen order ID"
        )

    # Find kitchen order
    kitchen_order = kitchen_collection.find_one(
        {"_id": ObjectId(kitchen_order_id)}
    )

    if not kitchen_order:
        raise HTTPException(
            status_code=404,
            detail="Kitchen order not found"
        )

    current_status = kitchen_order.get(
        "status",
        "pending"
    ).lower()

    # Order must be preparing first
    if current_status == "pending":
        raise HTTPException(
            status_code=400,
            detail="Kitchen order is still pending. Start the order first."
        )

    if current_status == "ready":
        raise HTTPException(
            status_code=400,
            detail="Kitchen order is already ready"
        )

    # Update status
    result = kitchen_collection.update_one(
        {"_id": ObjectId(kitchen_order_id)},
        {
            "$set": {
                "status": "ready"
            }
        }
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=400,
            detail="Kitchen order status could not be updated"
        )

    return {
        "status": "success",
        "message": "Kitchen order marked as ready",
        "kitchen_order_id": kitchen_order_id,
        "order_status": "ready"
    }