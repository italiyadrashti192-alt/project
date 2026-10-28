# from fastapi import FastAPI
# from app.db_config import check_database_connection

# app = FastAPI(
#     title="AI Food Management API"
# )


# @app.get("/")
# def home():
#     return {
#         "message": "Backend is running successfully"
#     }


# @app.get("/test-db")
# def test_database():

#     success, message = check_database_connection()

#     if success:
#         return {
#             "status": "success",
#             "message": message
#         }

#     return {
#         "status": "error",
#         "message": message
#     }


# from fastapi import FastAPI
# from app.db_config import check_database_connection
# from app.routes.ingredient_routes import router as ingredient_router
# from app.routes.inventory_routes import router as inventory_router
# from app.routes.supplier_routes import router as supplier_router
# # from app.routes.menu_routes import router as menu_router
# from app.routes.purchase_order_routes import router as purchase_order_router
# from app.routes.kitchen_routes import router as kitchen_router
# from app.routes import ai_routes

# app = FastAPI(
#     title="AI Food Management API"
# )



# # =====================================================
# # ROUTES
# # =====================================================

# app.include_router(ingredient_router)
# app.include_router(inventory_router)
# app.include_router(supplier_router)
# # app.include_router(menu_router)
# app.include_router(purchase_order_router)
# app.include_router(kitchen_router)
# app.include_router(ai_routes.router)
# # =====================================================
# # HOME
# # =====================================================

# @app.get("/")
# def home():
#     return {
#         "message": "Backend is running successfully"
#     }


# # =====================================================
# # DATABASE TEST
# # =====================================================

# @app.get("/test-db")
# def test_database():

#     success, message = check_database_connection()

#     if success:
#         return {
#             "status": "success",
#             "message": message
#         }

#     return {
#         "status": "error",
#         "message": message
#     }



# # from fastapi import FastAPI

# # from app.db_config import check_database_connection

# # from app.routes.ingredient_routes import router as ingredient_router
# # from app.routes.inventory_routes import router as inventory_router
# # from app.routes.supplier_routes import router as supplier_router
# # # from app.routes.menu_routes import router as menu_router
# # from app.routes.purchase_order_routes import router as purchase_order_router
# # from app.routes.kitchen_routes import router as kitchen_router
# # from app.routes import ai_routes


# # # =====================================================
# # # FASTAPI APP
# # # =====================================================

# # app = FastAPI(
# #     title="AI Food Management API"
# # )


# # # =====================================================
# # # DATABASE STARTUP CHECK
# # # =====================================================

# # @app.on_event("startup")
# # async def startup_event():
# #     """
# #     Check MongoDB when the application starts.

# #     MongoDB failure will NOT stop FastAPI from starting.
# #     """
# #     success, message = check_database_connection()

# #     if success:
# #         print(f"✅ {message}")
# #     else:
# #         print(f"⚠️ MongoDB is unavailable: {message}")
# #         print("⚠️ FastAPI will continue running.")


# # # =====================================================
# # # ROUTES
# # # =====================================================

# # app.include_router(ingredient_router)
# # app.include_router(inventory_router)
# # app.include_router(supplier_router)

# # # app.include_router(menu_router)

# # app.include_router(purchase_order_router)
# # app.include_router(kitchen_router)
# # app.include_router(ai_routes.router)


# # # =====================================================
# # # HOME
# # # =====================================================

# # @app.get("/")
# # def home():
# #     return {
# #         "message": "Backend is running successfully"
# #     }


# # # =====================================================
# # # DATABASE TEST
# # # =====================================================

# # @app.get("/test-db")
# # def test_database():

# #     success, message = check_database_connection()

# #     if success:
# #         return {
# #             "status": "success",
# #             "message": message
# #         }

# #     return {
# #         "status": "error",
# #         "message": message
# #     }


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db_config import check_database_connection

from app.routes.ingredient_routes import router as ingredient_router
from app.routes.inventory_routes import router as inventory_router
from app.routes.supplier_routes import router as supplier_router
# from app.routes.menu_routes import router as menu_router
from app.routes.purchase_order_routes import router as purchase_order_router
from app.routes.kitchen_routes import router as kitchen_router
from app.routes import ai_routes


app = FastAPI(
    title="AI Food Management API"
)


# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# ROUTES
# =====================================================

app.include_router(ingredient_router)
app.include_router(inventory_router)
app.include_router(supplier_router)
# app.include_router(menu_router)
app.include_router(purchase_order_router)
app.include_router(kitchen_router)
app.include_router(ai_routes.router)


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():
    return {
        "message": "Backend is running successfully"
    }


# =====================================================
# DATABASE TEST
# =====================================================

@app.get("/test-db")
def test_database():

    success, message = check_database_connection()

    if success:
        return {
            "status": "success",
            "message": message
        }

    return {
        "status": "error",
        "message": message
    }