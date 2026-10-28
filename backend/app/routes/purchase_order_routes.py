# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.purchase_order_model import (
#     PurchaseOrderCreate,
#     PurchaseOrderUpdate
# )

# router = APIRouter(
#     prefix="/purchase-orders",
#     tags=["Purchase Orders"]
# )

# purchase_orders_collection = db["purchase_orders"]


# # =========================
# # CREATE PURCHASE ORDER
# # =========================
# @router.post("/")
# async def create_purchase_order(order: PurchaseOrderCreate):

#     order_data = order.model_dump()

#     result = purchase_orders_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Purchase order created successfully",
#         "purchase_order_id": str(result.inserted_id)
#     }


# # =========================
# # GET ALL PURCHASE ORDERS
# # =========================
# @router.get("/")
# async def get_purchase_orders():

#     orders = []

#     for order in purchase_orders_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "purchase_orders": orders
#     }


# # =========================
# # GET PURCHASE ORDER BY ID
# # =========================
# @router.get("/{order_id}")
# async def get_purchase_order(order_id: str):

#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
#         )

#     order = purchase_orders_collection.find_one(
#         {"_id": ObjectId(order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "purchase_order": order
#     }


# # =========================
# # UPDATE PURCHASE ORDER
# # =========================
# @router.put("/{order_id}")
# async def update_purchase_order(
#     order_id: str,
#     order: PurchaseOrderUpdate
# ):

#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
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

#     result = purchase_orders_collection.update_one(
#         {"_id": ObjectId(order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Purchase order updated successfully"
#     }


# # =========================
# # DELETE PURCHASE ORDER
# # =========================
# @router.delete("/{order_id}")
# async def delete_purchase_order(order_id: str):

#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
#         )

#     result = purchase_orders_collection.delete_one(
#         {"_id": ObjectId(order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Purchase order deleted successfully"
#     }


# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.purchase_order_model import (
#     PurchaseOrderCreate,
#     PurchaseOrderUpdate
# )

# router = APIRouter(
#     prefix="/purchase-orders",
#     tags=["Purchase Orders"]
# )

# purchase_orders_collection = db["purchase_orders"]
# inventory_collection = db["inventory"]


# # =========================================================
# # CREATE PURCHASE ORDER
# # =========================================================
# @router.post("/")
# async def create_purchase_order(order: PurchaseOrderCreate):

#     order_data = order.model_dump()

#     result = purchase_orders_collection.insert_one(order_data)

#     return {
#         "status": "success",
#         "message": "Purchase order created successfully",
#         "purchase_order_id": str(result.inserted_id)
#     }


# # =========================================================
# # GET ALL PURCHASE ORDERS
# # =========================================================
# @router.get("/")
# async def get_purchase_orders():

#     orders = []

#     for order in purchase_orders_collection.find():

#         order["_id"] = str(order["_id"])

#         orders.append(order)

#     return {
#         "status": "success",
#         "count": len(orders),
#         "purchase_orders": orders
#     }


# # =========================================================
# # GET PURCHASE ORDER BY ID
# # =========================================================
# @router.get("/{order_id}")
# async def get_purchase_order(order_id: str):

#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
#         )

#     order = purchase_orders_collection.find_one(
#         {"_id": ObjectId(order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     order["_id"] = str(order["_id"])

#     return {
#         "status": "success",
#         "purchase_order": order
#     }


# # =========================================================
# # UPDATE PURCHASE ORDER
# # =========================================================
# @router.put("/{order_id}")
# async def update_purchase_order(
#     order_id: str,
#     order: PurchaseOrderUpdate
# ):

#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
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

#     result = purchase_orders_collection.update_one(
#         {"_id": ObjectId(order_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Purchase order updated successfully"
#     }


# # =========================================================
# # DELETE PURCHASE ORDER
# # =========================================================
# @router.delete("/{order_id}")
# async def delete_purchase_order(order_id: str):

#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
#         )

#     result = purchase_orders_collection.delete_one(
#         {"_id": ObjectId(order_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     return {
#         "status": "success",
#         "message": "Purchase order deleted successfully"
#     }


# # =========================================================
# # RECEIVE PURCHASE ORDER
# # =========================================================
# @router.post("/{order_id}/receive")
# async def receive_purchase_order(order_id: str):

#     # -----------------------------------------
#     # Check purchase order ID
#     # -----------------------------------------
#     if not ObjectId.is_valid(order_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid purchase order ID"
#         )

#     # -----------------------------------------
#     # Find purchase order
#     # -----------------------------------------
#     order = purchase_orders_collection.find_one(
#         {"_id": ObjectId(order_id)}
#     )

#     if not order:
#         raise HTTPException(
#             status_code=404,
#             detail="Purchase order not found"
#         )

#     # -----------------------------------------
#     # Check order status
#     # -----------------------------------------
#     if order.get("status") == "received":
#         raise HTTPException(
#             status_code=400,
#             detail="Purchase order has already been received"
#         )

#     # -----------------------------------------
#     # Get purchase order details
#     # -----------------------------------------
#     ingredient_name = order.get("ingredient_name")
#     quantity = order.get("quantity")
#     unit = order.get("unit")

#     if not ingredient_name or quantity is None or not unit:
#         raise HTTPException(
#             status_code=400,
#             detail="Purchase order has incomplete ingredient information"
#         )

#     # -----------------------------------------
#     # Find inventory using ingredient name
#     # -----------------------------------------
#     inventory = inventory_collection.find_one(
#         {"ingredient_name": ingredient_name}
#     )

#     if not inventory:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Inventory for {ingredient_name} not found"
#         )

#     # -----------------------------------------
#     # Calculate new quantity
#     # -----------------------------------------
#     old_quantity = inventory.get("quantity", 0)
#     new_quantity = old_quantity + quantity

#     # -----------------------------------------
#     # Update inventory
#     # -----------------------------------------
#     inventory_collection.update_one(
#         {"_id": inventory["_id"]},
#         {
#             "$set": {
#                 "quantity": new_quantity
#             }
#         }
#     )

#     # -----------------------------------------
#     # Update purchase order status
#     # -----------------------------------------
#     purchase_orders_collection.update_one(
#         {"_id": ObjectId(order_id)},
#         {
#             "$set": {
#                 "status": "received"
#             }
#         }
#     )

#     return {
#         "status": "success",
#         "message": "Purchase order received successfully",
#         "purchase_order_id": order_id,
#         "ingredient_name": ingredient_name,
#         "received_quantity": quantity,
#         "previous_stock": old_quantity,
#         "new_stock": new_quantity,
#         "unit": unit
#     }



from fastapi import APIRouter, HTTPException
from bson import ObjectId
import re

from app.db_config import db
from app.models.purchase_order_model import (
    PurchaseOrderCreate,
    PurchaseOrderUpdate
)

router = APIRouter(
    prefix="/purchase-orders",
    tags=["Purchase Orders"]
)

purchase_orders_collection = db["purchase_orders"]
inventory_collection = db["inventory"]


# =========================================================
# CREATE PURCHASE ORDER
# =========================================================
@router.post("/")
async def create_purchase_order(order: PurchaseOrderCreate):

    order_data = order.model_dump()

    result = purchase_orders_collection.insert_one(order_data)

    return {
        "status": "success",
        "message": "Purchase order created successfully",
        "purchase_order_id": str(result.inserted_id)
    }


# =========================================================
# GET ALL PURCHASE ORDERS
# =========================================================
@router.get("/")
async def get_purchase_orders():

    orders = []

    for order in purchase_orders_collection.find():

        order["_id"] = str(order["_id"])

        orders.append(order)

    return {
        "status": "success",
        "count": len(orders),
        "purchase_orders": orders
    }


# =========================================================
# GET PURCHASE ORDER BY ID
# =========================================================
@router.get("/{order_id}")
async def get_purchase_order(order_id: str):

    if not ObjectId.is_valid(order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid purchase order ID"
        )

    order = purchase_orders_collection.find_one(
        {"_id": ObjectId(order_id)}
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Purchase order not found"
        )

    order["_id"] = str(order["_id"])

    return {
        "status": "success",
        "purchase_order": order
    }


# =========================================================
# UPDATE PURCHASE ORDER
# =========================================================
@router.put("/{order_id}")
async def update_purchase_order(
    order_id: str,
    order: PurchaseOrderUpdate
):

    if not ObjectId.is_valid(order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid purchase order ID"
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

    result = purchase_orders_collection.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Purchase order not found"
        )

    return {
        "status": "success",
        "message": "Purchase order updated successfully"
    }


# =========================================================
# DELETE PURCHASE ORDER
# =========================================================
@router.delete("/{order_id}")
async def delete_purchase_order(order_id: str):

    if not ObjectId.is_valid(order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid purchase order ID"
        )

    result = purchase_orders_collection.delete_one(
        {"_id": ObjectId(order_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Purchase order not found"
        )

    return {
        "status": "success",
        "message": "Purchase order deleted successfully"
    }


# =========================================================
# RECEIVE PURCHASE ORDER → UPDATE INVENTORY
# =========================================================
@router.post("/{order_id}/receive")
async def receive_purchase_order(order_id: str):

    # -----------------------------------------
    # 1. Check purchase order ID
    # -----------------------------------------
    if not ObjectId.is_valid(order_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid purchase order ID"
        )

    # -----------------------------------------
    # 2. Find purchase order
    # -----------------------------------------
    order = purchase_orders_collection.find_one(
        {"_id": ObjectId(order_id)}
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Purchase order not found"
        )

    # -----------------------------------------
    # 3. Prevent duplicate receiving
    # -----------------------------------------
    if order.get("status", "").lower() == "received":

        raise HTTPException(
            status_code=400,
            detail="Purchase order has already been received"
        )

    # -----------------------------------------
    # 4. Get purchase order information
    # -----------------------------------------
    ingredient_name = order.get("ingredient_name")
    quantity = order.get("quantity")
    unit = order.get("unit")

    if not ingredient_name or quantity is None or not unit:

        raise HTTPException(
            status_code=400,
            detail="Purchase order has incomplete ingredient information"
        )

    # -----------------------------------------
    # 5. Validate quantity
    # -----------------------------------------
    if quantity <= 0:

        raise HTTPException(
            status_code=400,
            detail="Purchase order quantity must be greater than 0"
        )

    # -----------------------------------------
    # 6. Find inventory
    #    Case-insensitive ingredient matching
    # -----------------------------------------
    inventory = inventory_collection.find_one(
        {
            "ingredient_name": {
                "$regex": f"^{re.escape(ingredient_name)}$",
                "$options": "i"
            }
        }
    )

    if not inventory:

        raise HTTPException(
            status_code=404,
            detail=f"Inventory for '{ingredient_name}' not found"
        )

    # -----------------------------------------
    # 7. Check unit
    # -----------------------------------------
    inventory_unit = inventory.get("unit")

    if inventory_unit and inventory_unit.lower() != unit.lower():

        raise HTTPException(
            status_code=400,
            detail=(
                f"Unit mismatch. Inventory uses '{inventory_unit}' "
                f"but purchase order uses '{unit}'"
            )
        )

    # -----------------------------------------
    # 8. Get current inventory quantity
    # -----------------------------------------
    old_quantity = inventory.get("quantity", 0)

    # -----------------------------------------
    # 9. Calculate new inventory quantity
    # -----------------------------------------
    new_quantity = old_quantity + quantity

    # -----------------------------------------
    # 10. Update inventory
    # -----------------------------------------
    inventory_result = inventory_collection.update_one(
        {"_id": inventory["_id"]},
        {
            "$set": {
                "quantity": new_quantity
            }
        }
    )

    if inventory_result.modified_count == 0:

        raise HTTPException(
            status_code=500,
            detail="Failed to update inventory"
        )

    # -----------------------------------------
    # 11. Update purchase order status
    # -----------------------------------------
    purchase_order_result = purchase_orders_collection.update_one(
        {
            "_id": ObjectId(order_id),
            "status": {
                "$ne": "received"
            }
        },
        {
            "$set": {
                "status": "received"
            }
        }
    )

    if purchase_order_result.modified_count == 0:

        # Roll back inventory if PO status could not be changed
        inventory_collection.update_one(
            {"_id": inventory["_id"]},
            {
                "$set": {
                    "quantity": old_quantity
                }
            }
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to update purchase order status"
        )

    # -----------------------------------------
    # 12. Success response
    # -----------------------------------------
    return {
        "status": "success",
        "message": "Purchase order received and inventory updated successfully",
        "purchase_order_id": order_id,
        "ingredient_name": inventory.get(
            "ingredient_name",
            ingredient_name
        ),
        "received_quantity": quantity,
        "previous_stock": old_quantity,
        "new_stock": new_quantity,
        "unit": inventory_unit or unit,
        "purchase_order_status": "received"
    }   