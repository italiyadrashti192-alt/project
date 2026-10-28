from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.db_config import db
from app.models.supplier_model import (
    SupplierCreate,
    SupplierUpdate
)

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

suppliers_collection = db["suppliers"]


# =========================
# CREATE SUPPLIER
# =========================
@router.post("/")
async def create_supplier(supplier: SupplierCreate):

    supplier_data = supplier.model_dump()

    result = suppliers_collection.insert_one(supplier_data)

    return {
        "status": "success",
        "message": "Supplier created successfully",
        "supplier_id": str(result.inserted_id)
    }


# =========================
# GET ALL SUPPLIERS
# =========================
@router.get("/")
async def get_suppliers():

    suppliers = []

    for supplier in suppliers_collection.find():

        supplier["_id"] = str(supplier["_id"])

        suppliers.append(supplier)

    return {
        "status": "success",
        "count": len(suppliers),
        "suppliers": suppliers
    }


# =========================
# GET SUPPLIER BY ID
# =========================
@router.get("/{supplier_id}")
async def get_supplier(supplier_id: str):

    if not ObjectId.is_valid(supplier_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid supplier ID"
        )

    supplier = suppliers_collection.find_one(
        {"_id": ObjectId(supplier_id)}
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    supplier["_id"] = str(supplier["_id"])

    return {
        "status": "success",
        "supplier": supplier
    }


# =========================
# UPDATE SUPPLIER
# =========================
@router.put("/{supplier_id}")
async def update_supplier(
    supplier_id: str,
    supplier: SupplierUpdate
):

    if not ObjectId.is_valid(supplier_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid supplier ID"
        )

    update_data = {
        key: value
        for key, value in supplier.model_dump().items()
        if value is not None
    }

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    result = suppliers_collection.update_one(
        {"_id": ObjectId(supplier_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    return {
        "status": "success",
        "message": "Supplier updated successfully"
    }


# =========================
# DELETE SUPPLIER
# =========================
@router.delete("/{supplier_id}")
async def delete_supplier(supplier_id: str):

    if not ObjectId.is_valid(supplier_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid supplier ID"
        )

    result = suppliers_collection.delete_one(
        {"_id": ObjectId(supplier_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    return {
        "status": "success",
        "message": "Supplier deleted successfully"
    }