# from fastapi import APIRouter

# from app.db_config import db


# router = APIRouter(
#     prefix="/ai",
#     tags=["AI Analysis"]
# )

# # MongoDB collections
# inventory_collection = db["inventory"]
# kitchen_collection = db["kitchen_orders"]


# # =========================================================
# # AI INVENTORY ANALYSIS
# # =========================================================

# @router.get("/inventory-analysis")
# async def inventory_analysis():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     analysis = []

#     for inventory in inventory_items:

#         ingredient_name = inventory.get(
#             "ingredient_name"
#         )

#         current_stock = inventory.get(
#             "quantity", 0
#         )

#         minimum_stock = inventory.get(
#             "minimum_stock", 0
#         )

#         unit = inventory.get(
#             "unit", ""
#         )

#         # -------------------------------------------------
#         # Calculate estimated usage from kitchen orders
#         # -------------------------------------------------

#         total_usage = 0

#         kitchen_orders = kitchen_collection.find({
#             "ingredients.ingredient_name": ingredient_name
#         })

#         for order in kitchen_orders:

#             order_quantity = order.get(
#                 "quantity", 1
#             )

#             for ingredient in order.get(
#                 "ingredients", []
#             ):

#                 if ingredient.get(
#                     "ingredient_name"
#                 ) == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     # Quantity required per food item
#                     total_usage += (
#                         required * order_quantity
#                     )

#         # -------------------------------------------------
#         # Determine stock status
#         # -------------------------------------------------

#         remaining_stock = (
#             current_stock - total_usage
#         )

#         if current_stock <= minimum_stock:

#             stock_status = "critical"

#             recommendation = (
#                 f"Immediately reorder {ingredient_name}"
#             )

#         elif remaining_stock <= minimum_stock:

#             stock_status = "warning"

#             recommendation = (
#                 f"Consider restocking {ingredient_name}"
#             )

#         else:

#             stock_status = "healthy"

#             recommendation = (
#                 f"{ingredient_name} stock is sufficient"
#             )

#         # -------------------------------------------------
#         # Add analysis
#         # -------------------------------------------------

#         analysis.append({

#             "ingredient_name": ingredient_name,

#             "current_stock": current_stock,

#             "estimated_usage": total_usage,

#             "remaining_stock": remaining_stock,

#             "minimum_stock": minimum_stock,

#             "unit": unit,

#             "status": stock_status,

#             "recommendation": recommendation
#         })

#     # -----------------------------------------------------
#     # Response
#     # -----------------------------------------------------

#     return {
#         "status": "success",
#         "message": "AI inventory analysis completed",
#         "count": len(analysis),
#         "analysis": analysis
#     }



# from fastapi import APIRouter
# from bson import ObjectId

# from app.db_config import db


# router = APIRouter(
#     prefix="/ai",
#     tags=["AI Analysis"]
# )

# # MongoDB collections
# inventory_collection = db["inventory"]
# kitchen_collection = db["kitchen_orders"]


# # =========================================================
# # AI INVENTORY ANALYSIS
# # =========================================================

# @router.get("/inventory-analysis")
# async def inventory_analysis():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     analysis = []

#     for inventory in inventory_items:

#         ingredient_name = inventory.get(
#             "ingredient_name"
#         )

#         current_stock = inventory.get(
#             "quantity", 0
#         )

#         minimum_stock = inventory.get(
#             "minimum_stock", 0
#         )

#         unit = inventory.get(
#             "unit", ""
#         )

#         # -------------------------------------------------
#         # Calculate estimated usage from kitchen orders
#         # -------------------------------------------------

#         total_usage = 0

#         kitchen_orders = kitchen_collection.find({
#             "ingredients.ingredient_name": ingredient_name
#         })

#         for order in kitchen_orders:

#             order_quantity = order.get(
#                 "quantity", 1
#             )

#             for ingredient in order.get(
#                 "ingredients", []
#             ):

#                 if ingredient.get(
#                     "ingredient_name"
#                 ) == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     total_usage += (
#                         required * order_quantity
#                     )

#         # -------------------------------------------------
#         # Determine stock status
#         # -------------------------------------------------

#         remaining_stock = (
#             current_stock - total_usage
#         )

#         if current_stock <= minimum_stock:

#             stock_status = "critical"

#             recommendation = (
#                 f"Immediately reorder {ingredient_name}"
#             )

#         elif remaining_stock <= minimum_stock:

#             stock_status = "warning"

#             recommendation = (
#                 f"Consider restocking {ingredient_name}"
#             )

#         else:

#             stock_status = "healthy"

#             recommendation = (
#                 f"{ingredient_name} stock is sufficient"
#             )

#         # -------------------------------------------------
#         # Add analysis
#         # -------------------------------------------------

#         analysis.append({

#             "ingredient_name": ingredient_name,
#             "current_stock": current_stock,
#             "estimated_usage": total_usage,
#             "remaining_stock": remaining_stock,
#             "minimum_stock": minimum_stock,
#             "unit": unit,
#             "status": stock_status,
#             "recommendation": recommendation
#         })

#     return {
#         "status": "success",
#         "message": "AI inventory analysis completed",
#         "count": len(analysis),
#         "analysis": analysis
#     }


# # =========================================================
# # AI DEMAND PREDICTION
# # =========================================================

# @router.get("/demand-prediction")
# async def demand_prediction():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     predictions = []

#     # -----------------------------------------------------
#     # Analyze every inventory ingredient
#     # -----------------------------------------------------

#     for inventory in inventory_items:

#         ingredient_name = inventory.get(
#             "ingredient_name"
#         )

#         current_stock = inventory.get(
#             "quantity", 0
#         )

#         minimum_stock = inventory.get(
#             "minimum_stock", 0
#         )

#         unit = inventory.get(
#             "unit", ""
#         )

#         # -------------------------------------------------
#         # Find kitchen orders for this ingredient
#         # -------------------------------------------------

#         kitchen_orders = list(
#             kitchen_collection.find({
#                 "ingredients.ingredient_name": ingredient_name,
#                 "order_date": {
#                     "$exists": True
#                 }
#             })
#         )

#         # -------------------------------------------------
#         # Calculate usage by date
#         # -------------------------------------------------

#         daily_usage = {}

#         for order in kitchen_orders:

#             order_date = order.get(
#                 "order_date"
#             )

#             if not order_date:
#                 continue

#             # Convert MongoDB datetime to date
#             if hasattr(order_date, "date"):
#                 date_key = str(
#                     order_date.date()
#                 )
#             else:
#                 date_key = str(
#                     order_date
#                 )[:10]

#             order_quantity = order.get(
#                 "quantity", 1
#             )

#             for ingredient in order.get(
#                 "ingredients", []
#             ):

#                 if ingredient.get(
#                     "ingredient_name"
#                 ) == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     usage = (
#                         required * order_quantity
#                     )

#                     daily_usage[date_key] = (
#                         daily_usage.get(date_key, 0)
#                         + usage
#                     )

#         # -------------------------------------------------
#         # Calculate average daily usage
#         # -------------------------------------------------

#         if daily_usage:

#             total_usage = sum(
#                 daily_usage.values()
#             )

#             number_of_days = len(
#                 daily_usage
#             )

#             average_daily_usage = (
#                 total_usage / number_of_days
#             )

#         else:

#             total_usage = 0
#             number_of_days = 0
#             average_daily_usage = 0

#         # -------------------------------------------------
#         # Predict next 7 days
#         # -------------------------------------------------

#         predicted_7_day_demand = (
#             average_daily_usage * 7
#         )

#         # -------------------------------------------------
#         # Calculate expected remaining stock
#         # -------------------------------------------------

#         expected_stock_after_7_days = (
#             current_stock
#             - predicted_7_day_demand
#         )

#         # -------------------------------------------------
#         # AI recommendation
#         # -------------------------------------------------

#         if average_daily_usage == 0:

#             status = "no_usage_data"

#             recommendation = (
#                 f"No usage data available for "
#                 f"{ingredient_name}"
#             )

#         elif expected_stock_after_7_days <= 0:

#             status = "critical"

#             recommended_order = (
#                 predicted_7_day_demand
#                 - current_stock
#                 + minimum_stock
#             )

#             recommendation = (
#                 f"Immediately reorder approximately "
#                 f"{max(0, round(recommended_order, 2))} "
#                 f"{unit} of {ingredient_name}"
#             )

#         elif expected_stock_after_7_days <= minimum_stock:

#             status = "warning"

#             recommended_order = (
#                 predicted_7_day_demand
#                 - current_stock
#                 + minimum_stock
#             )

#             recommendation = (
#                 f"Consider ordering approximately "
#                 f"{max(0, round(recommended_order, 2))} "
#                 f"{unit} of {ingredient_name}"
#             )

#         else:

#             status = "healthy"

#             recommendation = (
#                 f"Current {ingredient_name} stock "
#                 f"should be sufficient for 7 days"
#             )

#         # -------------------------------------------------
#         # Add prediction
#         # -------------------------------------------------

#         predictions.append({

#             "ingredient_name": ingredient_name,

#             "current_stock": current_stock,

#             "unit": unit,

#             "days_with_usage_data": number_of_days,

#             "total_historical_usage": round(
#                 total_usage, 2
#             ),

#             "average_daily_usage": round(
#                 average_daily_usage, 2
#             ),

#             "predicted_7_day_demand": round(
#                 predicted_7_day_demand, 2
#             ),

#             "expected_stock_after_7_days": round(
#                 expected_stock_after_7_days, 2
#             ),

#             "minimum_stock": minimum_stock,

#             "status": status,

#             "recommendation": recommendation
#         })

#     # -----------------------------------------------------
#     # Response
#     # -----------------------------------------------------

#     return {

#         "status": "success",

#         "message": (
#             "AI demand prediction completed"
#         ),

#         "count": len(predictions),

#         "predictions": predictions
#     }
# # =========================================================
# # AI REORDER RECOMMENDATION
# # =========================================================

# @router.get("/reorder-recommendation")
# async def reorder_recommendation():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     suppliers_collection = db["suppliers"]

#     recommendations = []

#     for inventory in inventory_items:

#         ingredient_name = inventory.get("ingredient_name")
#         current_stock = inventory.get("quantity", 0)
#         minimum_stock = inventory.get("minimum_stock", 0)
#         unit = inventory.get("unit", "")
#         supplier_name = inventory.get("supplier")

#         # -------------------------------------------------
#         # Find kitchen orders
#         # -------------------------------------------------

#         kitchen_orders = list(
#             kitchen_collection.find({
#                 "ingredients.ingredient_name": ingredient_name,
#                 "order_date": {"$exists": True}
#             })
#         )

#         daily_usage = {}

#         for order in kitchen_orders:

#             order_date = order.get("order_date")

#             if not order_date:
#                 continue

#             if hasattr(order_date, "date"):
#                 date_key = str(order_date.date())
#             else:
#                 date_key = str(order_date)[:10]

#             order_quantity = order.get("quantity", 1)

#             for ingredient in order.get("ingredients", []):

#                 if ingredient.get("ingredient_name") == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     usage = required * order_quantity

#                     daily_usage[date_key] = (
#                         daily_usage.get(date_key, 0)
#                         + usage
#                     )

#         # -------------------------------------------------
#         # Average daily usage
#         # -------------------------------------------------

#         if daily_usage:

#             total_usage = sum(daily_usage.values())

#             days = len(daily_usage)

#             average_daily_usage = (
#                 total_usage / days
#             )

#         else:

#             average_daily_usage = 0

#         # -------------------------------------------------
#         # 7-day predicted demand
#         # -------------------------------------------------

#         predicted_demand = (
#             average_daily_usage * 7
#         )

#         # -------------------------------------------------
#         # Recommended quantity
#         # -------------------------------------------------

#         recommended_quantity = (
#             predicted_demand
#             + minimum_stock
#             - current_stock
#         )

#         if recommended_quantity <= 0:
#             continue

#         # -------------------------------------------------
#         # Find supplier
#         # -------------------------------------------------

#         # supplier = None

#         # if supplier_name:

#         #     supplier = suppliers_collection.find_one({
#         #         "name": supplier_name
#         #     })

#             # -----------------------------------------------------
# # Find supplier by ID OR name
# # -----------------------------------------------------

# supplier = None

# if supplier_name:

#     # First try supplier ID
#     if ObjectId.is_valid(supplier_name):

#         supplier = suppliers_collection.find_one({
#             "_id": ObjectId(supplier_name)
#         })

#     # If not found, try supplier name
#     if not supplier:

#         supplier = suppliers_collection.find_one({
#             "name": supplier_name
#         })

#         # -------------------------------------------------
#         # Supplier not found
#         # -------------------------------------------------

#         if not supplier:

#             recommendations.append({

#                 "ingredient_name": ingredient_name,

#                 "recommended_quantity": round(
#                     recommended_quantity, 2
#                 ),

#                 "unit": unit,

#                 "supplier": supplier_name,

#                 "status": "supplier_not_found",

#                 "message": (
#                     f"Supplier not found for "
#                     f"{ingredient_name}"
#                 )
#             })

#             continue

#         # -------------------------------------------------
#         # Supplier found
#         # -------------------------------------------------

#         recommendations.append({

#             "ingredient_name": ingredient_name,

#             "current_stock": current_stock,

#             "minimum_stock": minimum_stock,

#             "unit": unit,

#             "average_daily_usage": round(
#                 average_daily_usage, 2
#             ),

#             "predicted_7_day_demand": round(
#                 predicted_demand, 2
#             ),

#             "recommended_quantity": round(
#                 recommended_quantity, 2
#             ),

#             "supplier_id": str(
#                 supplier["_id"]
#             ),

#             "supplier_name": supplier.get(
#                 "name"
#             ),

#             "supplier_phone": supplier.get(
#                 "phone"
#             ),

#             "status": "reorder_recommended",

#             "message": (
#                 f"Order approximately "
#                 f"{round(recommended_quantity, 2)} "
#                 f"{unit} of {ingredient_name}"
#             )
#         })

#     return {

#         "status": "success",

#         "message": (
#             "AI reorder recommendation completed"
#         ),

#         "count": len(recommendations),

#         "recommendations": recommendations
#     }

# # =========================================================
# # AI CREATE PURCHASE ORDER
# # =========================================================

# @router.post("/create-reorder/{ingredient_name}")
# async def create_ai_reorder(ingredient_name: str):

#     suppliers_collection = db["suppliers"]
#     purchase_orders_collection = db["purchase_orders"]

#     # -----------------------------------------------------
#     # Find inventory
#     # -----------------------------------------------------

#     inventory = inventory_collection.find_one({
#         "ingredient_name": ingredient_name
#     })

#     if not inventory:

#         return {
#             "status": "failed",
#             "message": (
#                 f"Inventory not found for "
#                 f"{ingredient_name}"
#             )
#         }

#     current_stock = inventory.get(
#         "quantity", 0
#     )

#     minimum_stock = inventory.get(
#         "minimum_stock", 0
#     )

#     unit = inventory.get(
#         "unit", ""
#     )

#     supplier_name = inventory.get(
#         "supplier"
#     )

#     # -----------------------------------------------------
#     # Find kitchen orders
#     # -----------------------------------------------------

#     kitchen_orders = list(
#         kitchen_collection.find({
#             "ingredients.ingredient_name": ingredient_name,
#             "order_date": {"$exists": True}
#         })
#     )

#     daily_usage = {}

#     for order in kitchen_orders:

#         order_date = order.get(
#             "order_date"
#         )

#         if not order_date:
#             continue

#         if hasattr(order_date, "date"):

#             date_key = str(
#                 order_date.date()
#             )

#         else:

#             date_key = str(
#                 order_date
#             )[:10]

#         order_quantity = order.get(
#             "quantity", 1
#         )

#         for ingredient in order.get(
#             "ingredients", []
#         ):

#             if ingredient.get(
#                 "ingredient_name"
#             ) == ingredient_name:

#                 required = ingredient.get(
#                     "quantity_required", 0
#                 )

#                 usage = (
#                     required * order_quantity
#                 )

#                 daily_usage[date_key] = (
#                     daily_usage.get(
#                         date_key, 0
#                     ) + usage
#                 )

#     # -----------------------------------------------------
#     # Calculate average usage
#     # -----------------------------------------------------

#     if not daily_usage:

#         return {
#             "status": "failed",
#             "message": (
#                 f"No usage data available "
#                 f"for {ingredient_name}"
#             )
#         }

#     total_usage = sum(
#         daily_usage.values()
#     )

#     number_of_days = len(
#         daily_usage
#     )

#     average_daily_usage = (
#         total_usage / number_of_days
#     )

#     # -----------------------------------------------------
#     # Predict 7-day demand
#     # -----------------------------------------------------

#     predicted_demand = (
#         average_daily_usage * 7
#     )

#     # -----------------------------------------------------
#     # Calculate reorder quantity
#     # -----------------------------------------------------

#     recommended_quantity = (
#         predicted_demand
#         + minimum_stock
#         - current_stock
#     )

#     if recommended_quantity <= 0:

#         return {
#             "status": "success",
#             "message": (
#                 f"No reorder required for "
#                 f"{ingredient_name}"
#             ),
#             "current_stock": current_stock,
#             "predicted_demand": round(
#                 predicted_demand, 2
#             )
#         }

#     # -----------------------------------------------------
#     # Find supplier
#     # -----------------------------------------------------

#     if not supplier_name:

#         return {
#             "status": "failed",
#             "message": (
#                 f"No supplier assigned to "
#                 f"{ingredient_name}"
#             )
#         }

#     supplier = suppliers_collection.find_one({
#         "name": supplier_name
#     })

#     if not supplier:

#         return {
#             "status": "failed",
#             "message": (
#                 f"Supplier '{supplier_name}' "
#                 f"not found"
#             )
#         }

#     # -----------------------------------------------------
#     # Create purchase order
#     # -----------------------------------------------------

#     purchase_order = {

#         "supplier_id": str(
#             supplier["_id"]
#         ),

#         "ingredient_name": ingredient_name,

#         "quantity": round(
#             recommended_quantity, 2
#         ),

#         "unit": unit,

#         "status": "pending",

#         "source": "AI",

#         "average_daily_usage": round(
#             average_daily_usage, 2
#         ),

#         "predicted_7_day_demand": round(
#             predicted_demand, 2
#         )
#     }

#     result = purchase_orders_collection.insert_one(
#         purchase_order
#     )

#     return {

#         "status": "success",

#         "message": (
#             "AI reorder purchase order "
#             "created successfully"
#         ),

#         "purchase_order_id": str(
#             result.inserted_id
#         ),

#         "ingredient_name": ingredient_name,

#         "quantity": round(
#             recommended_quantity, 2
#         ),

#         "unit": unit,

#         "supplier_id": str(
#             supplier["_id"]
#         ),

#         "supplier_name": supplier.get(
#             "name"
#         ),

#         "source": "AI",

#         "status": "pending"
#     }

# from fastapi import APIRouter
# from bson import ObjectId

# from app.db_config import db


# router = APIRouter(
#     prefix="/ai",
#     tags=["AI Analysis"]
# )

# # =========================================================
# # MONGODB COLLECTIONS
# # =========================================================

# inventory_collection = db["inventory"]
# kitchen_collection = db["kitchen_orders"]
# suppliers_collection = db["suppliers"]
# purchase_orders_collection = db["purchase_orders"]


# # =========================================================
# # HELPER: FIND SUPPLIER BY ID OR NAME
# # =========================================================

# def find_supplier(supplier_value):

#     if not supplier_value:
#         return None

#     supplier_value = str(supplier_value).strip()

#     # -----------------------------------------------------
#     # Try MongoDB ObjectId
#     # -----------------------------------------------------

#     if ObjectId.is_valid(supplier_value):

#         supplier = suppliers_collection.find_one({
#             "_id": ObjectId(supplier_value)
#         })

#         if supplier:
#             return supplier

#     # -----------------------------------------------------
#     # Try supplier name
#     # -----------------------------------------------------

#     supplier = suppliers_collection.find_one({
#         "name": supplier_value
#     })

#     if supplier:
#         return supplier

#     return None


# # =========================================================
# # AI INVENTORY ANALYSIS
# # =========================================================

# @router.get("/inventory-analysis")
# async def inventory_analysis():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     analysis = []

#     for inventory in inventory_items:

#         ingredient_name = inventory.get(
#             "ingredient_name"
#         )

#         current_stock = inventory.get(
#             "quantity", 0
#         )

#         minimum_stock = inventory.get(
#             "minimum_stock", 0
#         )

#         unit = inventory.get(
#             "unit", ""
#         )

#         total_usage = 0

#         kitchen_orders = kitchen_collection.find({
#             "ingredients.ingredient_name": ingredient_name
#         })

#         for order in kitchen_orders:

#             order_quantity = order.get(
#                 "quantity", 1
#             )

#             for ingredient in order.get(
#                 "ingredients", []
#             ):

#                 if ingredient.get(
#                     "ingredient_name"
#                 ) == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     total_usage += (
#                         required * order_quantity
#                     )

#         remaining_stock = (
#             current_stock - total_usage
#         )

#         if current_stock <= minimum_stock:

#             stock_status = "critical"

#             recommendation = (
#                 f"Immediately reorder {ingredient_name}"
#             )

#         elif remaining_stock <= minimum_stock:

#             stock_status = "warning"

#             recommendation = (
#                 f"Consider restocking {ingredient_name}"
#             )

#         else:

#             stock_status = "healthy"

#             recommendation = (
#                 f"{ingredient_name} stock is sufficient"
#             )

#         analysis.append({

#             "ingredient_name": ingredient_name,

#             "current_stock": current_stock,

#             "estimated_usage": total_usage,

#             "remaining_stock": remaining_stock,

#             "minimum_stock": minimum_stock,

#             "unit": unit,

#             "status": stock_status,

#             "recommendation": recommendation
#         })

#     return {

#         "status": "success",

#         "message": (
#             "AI inventory analysis completed"
#         ),

#         "count": len(analysis),

#         "analysis": analysis
#     }


# # =========================================================
# # AI DEMAND PREDICTION
# # =========================================================

# @router.get("/demand-prediction")
# async def demand_prediction():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     predictions = []

#     for inventory in inventory_items:

#         ingredient_name = inventory.get(
#             "ingredient_name"
#         )

#         current_stock = inventory.get(
#             "quantity", 0
#         )

#         minimum_stock = inventory.get(
#             "minimum_stock", 0
#         )

#         unit = inventory.get(
#             "unit", ""
#         )

#         kitchen_orders = list(
#             kitchen_collection.find({
#                 "ingredients.ingredient_name": ingredient_name,
#                 "order_date": {
#                     "$exists": True
#                 }
#             })
#         )

#         daily_usage = {}

#         for order in kitchen_orders:

#             order_date = order.get(
#                 "order_date"
#             )

#             if not order_date:
#                 continue

#             if hasattr(order_date, "date"):

#                 date_key = str(
#                     order_date.date()
#                 )

#             else:

#                 date_key = str(
#                     order_date
#                 )[:10]

#             order_quantity = order.get(
#                 "quantity", 1
#             )

#             for ingredient in order.get(
#                 "ingredients", []
#             ):

#                 if ingredient.get(
#                     "ingredient_name"
#                 ) == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     usage = (
#                         required * order_quantity
#                     )

#                     daily_usage[date_key] = (
#                         daily_usage.get(
#                             date_key, 0
#                         ) + usage
#                     )

#         if daily_usage:

#             total_usage = sum(
#                 daily_usage.values()
#             )

#             number_of_days = len(
#                 daily_usage
#             )

#             average_daily_usage = (
#                 total_usage / number_of_days
#             )

#         else:

#             total_usage = 0
#             number_of_days = 0
#             average_daily_usage = 0

#         predicted_7_day_demand = (
#             average_daily_usage * 7
#         )

#         expected_stock_after_7_days = (
#             current_stock
#             - predicted_7_day_demand
#         )

#         if average_daily_usage == 0:

#             status = "no_usage_data"

#             recommendation = (
#                 f"No usage data available for "
#                 f"{ingredient_name}"
#             )

#         elif expected_stock_after_7_days <= 0:

#             status = "critical"

#             recommended_order = (
#                 predicted_7_day_demand
#                 - current_stock
#                 + minimum_stock
#             )

#             recommendation = (
#                 f"Immediately reorder approximately "
#                 f"{max(0, round(recommended_order, 2))} "
#                 f"{unit} of {ingredient_name}"
#             )

#         elif expected_stock_after_7_days <= minimum_stock:

#             status = "warning"

#             recommended_order = (
#                 predicted_7_day_demand
#                 - current_stock
#                 + minimum_stock
#             )

#             recommendation = (
#                 f"Consider ordering approximately "
#                 f"{max(0, round(recommended_order, 2))} "
#                 f"{unit} of {ingredient_name}"
#             )

#         else:

#             status = "healthy"

#             recommendation = (
#                 f"Current {ingredient_name} stock "
#                 f"should be sufficient for 7 days"
#             )

#         predictions.append({

#             "ingredient_name": ingredient_name,

#             "current_stock": current_stock,

#             "unit": unit,

#             "days_with_usage_data": number_of_days,

#             "total_historical_usage": round(
#                 total_usage, 2
#             ),

#             "average_daily_usage": round(
#                 average_daily_usage, 2
#             ),

#             "predicted_7_day_demand": round(
#                 predicted_7_day_demand, 2
#             ),

#             "expected_stock_after_7_days": round(
#                 expected_stock_after_7_days, 2
#             ),

#             "minimum_stock": minimum_stock,

#             "status": status,

#             "recommendation": recommendation
#         })

#     return {

#         "status": "success",

#         "message": (
#             "AI demand prediction completed"
#         ),

#         "count": len(predictions),

#         "predictions": predictions
#     }


# # =========================================================
# # AI REORDER RECOMMENDATION
# # =========================================================

# @router.get("/reorder-recommendation")
# async def reorder_recommendation():

#     inventory_items = list(
#         inventory_collection.find()
#     )

#     recommendations = []

#     for inventory in inventory_items:

#         ingredient_name = inventory.get(
#             "ingredient_name"
#         )

#         current_stock = inventory.get(
#             "quantity", 0
#         )

#         minimum_stock = inventory.get(
#             "minimum_stock", 0
#         )

#         unit = inventory.get(
#             "unit", ""
#         )

#         supplier_value = inventory.get(
#             "supplier"
#         )

#         kitchen_orders = list(
#             kitchen_collection.find({
#                 "ingredients.ingredient_name": ingredient_name,
#                 "order_date": {
#                     "$exists": True
#                 }
#             })
#         )

#         daily_usage = {}

#         for order in kitchen_orders:

#             order_date = order.get(
#                 "order_date"
#             )

#             if not order_date:
#                 continue

#             if hasattr(order_date, "date"):

#                 date_key = str(
#                     order_date.date()
#                 )

#             else:

#                 date_key = str(
#                     order_date
#                 )[:10]

#             order_quantity = order.get(
#                 "quantity", 1
#             )

#             for ingredient in order.get(
#                 "ingredients", []
#             ):

#                 if ingredient.get(
#                     "ingredient_name"
#                 ) == ingredient_name:

#                     required = ingredient.get(
#                         "quantity_required", 0
#                     )

#                     usage = (
#                         required * order_quantity
#                     )

#                     daily_usage[date_key] = (
#                         daily_usage.get(
#                             date_key, 0
#                         ) + usage
#                     )

#         if not daily_usage:
#             continue

#         total_usage = sum(
#             daily_usage.values()
#         )

#         number_of_days = len(
#             daily_usage
#         )

#         average_daily_usage = (
#             total_usage / number_of_days
#         )

#         predicted_demand = (
#             average_daily_usage * 7
#         )

#         recommended_quantity = (
#             predicted_demand
#             + minimum_stock
#             - current_stock
#         )

#         if recommended_quantity <= 0:
#             continue

#         # -------------------------------------------------
#         # Find supplier by ID OR NAME
#         # -------------------------------------------------

#         supplier = find_supplier(
#             supplier_value
#         )

#         if not supplier:

#             recommendations.append({

#                 "ingredient_name": ingredient_name,

#                 "current_stock": current_stock,

#                 "recommended_quantity": round(
#                     recommended_quantity, 2
#                 ),

#                 "unit": unit,

#                 "supplier_value": supplier_value,

#                 "status": "supplier_not_found",

#                 "message": (
#                     f"Supplier '{supplier_value}' "
#                     f"not found"
#                 )
#             })

#             continue

#         recommendations.append({

#             "ingredient_name": ingredient_name,

#             "current_stock": current_stock,

#             "minimum_stock": minimum_stock,

#             "unit": unit,

#             "average_daily_usage": round(
#                 average_daily_usage, 2
#             ),

#             "predicted_7_day_demand": round(
#                 predicted_demand, 2
#             ),

#             "recommended_quantity": round(
#                 recommended_quantity, 2
#             ),

#             "supplier_id": str(
#                 supplier["_id"]
#             ),

#             "supplier_name": supplier.get(
#                 "name"
#             ),

#             "supplier_phone": supplier.get(
#                 "phone"
#             ),

#             "status": "reorder_recommended",

#             "message": (
#                 f"Order approximately "
#                 f"{round(recommended_quantity, 2)} "
#                 f"{unit} of {ingredient_name} "
#                 f"from {supplier.get('name')}"
#             )
#         })

#     return {

#         "status": "success",

#         "message": (
#             "AI reorder recommendation completed"
#         ),

#         "count": len(recommendations),

#         "recommendations": recommendations
#     }


# # =========================================================
# # AI CREATE PURCHASE ORDER
# # =========================================================

# @router.post("/create-reorder/{ingredient_name}")
# async def create_ai_reorder(
#     ingredient_name: str
# ):

#     # -----------------------------------------------------
#     # Find inventory
#     # -----------------------------------------------------

#     inventory = inventory_collection.find_one({
#         "ingredient_name": ingredient_name
#     })

#     if not inventory:

#         return {

#             "status": "failed",

#             "message": (
#                 f"Inventory not found for "
#                 f"{ingredient_name}"
#             )
#         }

#     current_stock = inventory.get(
#         "quantity", 0
#     )

#     minimum_stock = inventory.get(
#         "minimum_stock", 0
#     )

#     unit = inventory.get(
#         "unit", ""
#     )

#     supplier_value = inventory.get(
#         "supplier"
#     )

#     # -----------------------------------------------------
#     # Find kitchen orders
#     # -----------------------------------------------------

#     kitchen_orders = list(
#         kitchen_collection.find({
#             "ingredients.ingredient_name": ingredient_name,
#             "order_date": {
#                 "$exists": True
#             }
#         })
#     )

#     daily_usage = {}

#     for order in kitchen_orders:

#         order_date = order.get(
#             "order_date"
#         )

#         if not order_date:
#             continue

#         if hasattr(order_date, "date"):

#             date_key = str(
#                 order_date.date()
#             )

#         else:

#             date_key = str(
#                 order_date
#             )[:10]

#         order_quantity = order.get(
#             "quantity", 1
#         )

#         for ingredient in order.get(
#             "ingredients", []
#         ):

#             if ingredient.get(
#                 "ingredient_name"
#             ) == ingredient_name:

#                 required = ingredient.get(
#                     "quantity_required", 0
#                 )

#                 usage = (
#                     required * order_quantity
#                 )

#                 daily_usage[date_key] = (
#                     daily_usage.get(
#                         date_key, 0
#                     ) + usage
#                 )

#     if not daily_usage:

#         return {

#             "status": "failed",

#             "message": (
#                 f"No usage data available for "
#                 f"{ingredient_name}"
#             )
#         }

#     total_usage = sum(
#         daily_usage.values()
#     )

#     number_of_days = len(
#         daily_usage
#     )

#     average_daily_usage = (
#         total_usage / number_of_days
#     )

#     predicted_demand = (
#         average_daily_usage * 7
#     )

#     recommended_quantity = (
#         predicted_demand
#         + minimum_stock
#         - current_stock
#     )

#     if recommended_quantity <= 0:

#         return {

#             "status": "success",

#             "message": (
#                 f"No reorder required for "
#                 f"{ingredient_name}"
#             ),

#             "current_stock": current_stock,

#             "predicted_demand": round(
#                 predicted_demand, 2
#             )
#         }

#     # -----------------------------------------------------
#     # Find supplier by ID OR NAME
#     # -----------------------------------------------------

#     supplier = find_supplier(
#         supplier_value
#     )

#     if not supplier:

#         return {

#             "status": "failed",

#             "message": (
#                 f"Supplier '{supplier_value}' "
#                 f"not found"
#             )
#         }

#     # -----------------------------------------------------
#     # Create Purchase Order
#     # -----------------------------------------------------

#     purchase_order = {

#         "supplier_id": str(
#             supplier["_id"]
#         ),

#         "ingredient_name": ingredient_name,

#         "quantity": round(
#             recommended_quantity, 2
#         ),

#         "unit": unit,

#         "status": "pending",

#         "source": "AI",

#         "average_daily_usage": round(
#             average_daily_usage, 2
#         ),

#         "predicted_7_day_demand": round(
#             predicted_demand, 2
#         )
#     }

#     result = purchase_orders_collection.insert_one(
#         purchase_order
#     )

#     return {

#         "status": "success",

#         "message": (
#             "AI reorder purchase order "
#             "created successfully"
#         ),

#         "purchase_order_id": str(
#             result.inserted_id
#         ),

#         "ingredient_name": ingredient_name,

#         "quantity": round(
#             recommended_quantity, 2
#         ),

#         "unit": unit,

#         "supplier_id": str(
#             supplier["_id"]
#         ),

#         "supplier_name": supplier.get(
#             "name"
#         ),

#         "source": "AI",

#         "status": "pending"
#     }

from fastapi import APIRouter
from app.db_config import db

router = APIRouter(
    prefix="/ai",
    tags=["AI Analysis"]
)

inventory_collection = db["inventory"]
kitchen_collection = db["kitchen_orders"]


@router.get("/inventory-analysis")
async def inventory_analysis():

    inventory = list(inventory_collection.find())
    kitchen_orders = list(kitchen_collection.find())

    analysis = []

    for item in inventory:

        ingredient_name = item.get("ingredient_name", "")
        current_stock = item.get("quantity", 0)
        minimum_stock = item.get("minimum_stock", 0)
        unit = item.get("unit", "")

        total_used = 0

        # Check kitchen orders
        for order in kitchen_orders:

            ingredients = order.get("ingredients", [])

            for ingredient in ingredients:

                order_ingredient = ingredient.get(
                    "ingredient_name",
                    ""
                )

                # Case-insensitive ingredient matching
                if (
                    order_ingredient.strip().lower()
                    == ingredient_name.strip().lower()
                ):
                    total_used += ingredient.get(
                        "quantity_required",
                        0
                    )

        # Determine stock status
        if current_stock <= minimum_stock:
            stock_status = "low_stock"
        else:
            stock_status = "normal"

        # Simple demand classification
        if total_used == 0:
            demand = "no_usage_data"
        elif total_used >= 20:
            demand = "high"
        elif total_used >= 10:
            demand = "medium"
        else:
            demand = "low"

        analysis.append({
            "ingredient_name": ingredient_name,
            "current_stock": current_stock,
            "minimum_stock": minimum_stock,
            "unit": unit,
            "total_used": total_used,
            "stock_status": stock_status,
            "demand": demand
        })

    return {
        "status": "success",
        "count": len(analysis),
        "analysis": analysis
    }