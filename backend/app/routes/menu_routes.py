# from fastapi import APIRouter, HTTPException
# from bson import ObjectId

# from app.db_config import db
# from app.models.menu_model import MenuCreate, MenuUpdate

# router = APIRouter(
#     prefix="/menu",
#     tags=["Menu"]
# )

# menu_collection = db["menu"]


# # =========================
# # CREATE MENU ITEM
# # =========================
# @router.post("/")
# async def create_menu(menu: MenuCreate):

#     menu_data = menu.model_dump()

#     result = menu_collection.insert_one(menu_data)

#     return {
#         "status": "success",
#         "message": "Menu item created successfully",
#         "menu_id": str(result.inserted_id)
#     }


# # =========================
# # GET ALL MENU ITEMS
# # =========================
# @router.get("/")
# async def get_menu():

#     menu_items = []

#     for item in menu_collection.find():

#         item["_id"] = str(item["_id"])

#         menu_items.append(item)

#     return {
#         "status": "success",
#         "count": len(menu_items),
#         "menu": menu_items
#     }


# # =========================
# # GET MENU ITEM BY ID
# # =========================
# @router.get("/{menu_id}")
# async def get_menu_item(menu_id: str):

#     if not ObjectId.is_valid(menu_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid menu ID"
#         )

#     item = menu_collection.find_one(
#         {"_id": ObjectId(menu_id)}
#     )

#     if not item:
#         raise HTTPException(
#             status_code=404,
#             detail="Menu item not found"
#         )

#     item["_id"] = str(item["_id"])

#     return {
#         "status": "success",
#         "menu": item
#     }


# # =========================
# # UPDATE MENU ITEM
# # =========================
# @router.put("/{menu_id}")
# async def update_menu_item(
#     menu_id: str,
#     menu: MenuUpdate
# ):

#     if not ObjectId.is_valid(menu_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid menu ID"
#         )

#     update_data = {
#         key: value
#         for key, value in menu.model_dump().items()
#         if value is not None
#     }

#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="No data provided for update"
#         )

#     result = menu_collection.update_one(
#         {"_id": ObjectId(menu_id)},
#         {"$set": update_data}
#     )

#     if result.matched_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Menu item not found"
#         )

#     return {
#         "status": "success",
#         "message": "Menu item updated successfully"
#     }


# # =========================
# # DELETE MENU ITEM
# # =========================
# @router.delete("/{menu_id}")
# async def delete_menu_item(menu_id: str):

#     if not ObjectId.is_valid(menu_id):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid menu ID"
#         )

#     result = menu_collection.delete_one(
#         {"_id": ObjectId(menu_id)}
#     )

#     if result.deleted_count == 0:
#         raise HTTPException(
#             status_code=404,
#             detail="Menu item not found"
#         )

#     return {
#         "status": "success",
#         "message": "Menu item deleted successfully"
#     }