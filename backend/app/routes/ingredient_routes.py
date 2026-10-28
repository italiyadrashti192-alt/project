from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.db_config import db
from app.models.ingredient_model import (
    IngredientCreate,
    IngredientUpdate
)


router = APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"]
)


ingredients_collection = db["ingredients"]


# =====================================================
# CREATE INGREDIENT
# =====================================================

@router.post("/")
def create_ingredient(ingredient: IngredientCreate):

    existing = ingredients_collection.find_one({
        "name": ingredient.name
    })

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Ingredient already exists"
        )

    ingredient_data = ingredient.model_dump()

    result = ingredients_collection.insert_one(
        ingredient_data
    )

    return {
        "status": "success",
        "message": "Ingredient created successfully",
        "ingredient_id": str(result.inserted_id)
    }


# =====================================================
# GET ALL INGREDIENTS
# =====================================================

@router.get("/")
def get_all_ingredients():

    ingredients = list(
        ingredients_collection.find()
    )

    for ingredient in ingredients:
        ingredient["_id"] = str(ingredient["_id"])

    return {
        "status": "success",
        "count": len(ingredients),
        "ingredients": ingredients
    }


# =====================================================
# GET SINGLE INGREDIENT
# =====================================================

@router.get("/{ingredient_id}")
def get_ingredient(ingredient_id: str):

    if not ObjectId.is_valid(ingredient_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid ingredient ID"
        )

    ingredient = ingredients_collection.find_one({
        "_id": ObjectId(ingredient_id)
    })

    if not ingredient:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    ingredient["_id"] = str(ingredient["_id"])

    return {
        "status": "success",
        "ingredient": ingredient
    }


# =====================================================
# UPDATE INGREDIENT
# =====================================================

@router.put("/{ingredient_id}")
def update_ingredient(
    ingredient_id: str,
    ingredient: IngredientUpdate
):

    if not ObjectId.is_valid(ingredient_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid ingredient ID"
        )

    update_data = {
        key: value
        for key, value in ingredient.model_dump().items()
        if value is not None
    }

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    result = ingredients_collection.update_one(
        {"_id": ObjectId(ingredient_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    return {
        "status": "success",
        "message": "Ingredient updated successfully"
    }


# =====================================================
# DELETE INGREDIENT
# =====================================================

@router.delete("/{ingredient_id}")
def delete_ingredient(ingredient_id: str):

    if not ObjectId.is_valid(ingredient_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid ingredient ID"
        )

    result = ingredients_collection.delete_one({
        "_id": ObjectId(ingredient_id)
    })

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    return {
        "status": "success",
        "message": "Ingredient deleted successfully"
    }