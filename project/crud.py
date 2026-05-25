from fastapi import APIRouter, HTTPException
from project.models import Product
from typing import List
import json

router = APIRouter()

def load_data():
    with open("project/product.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("project/product.json", "w") as f:
        json.dump(data, f, indent=4)

@router.post("/products", status_code=201, response_model=Product)
def create_product(product: Product):
    products = load_data()
    for p in products:
        if p["id"] == product.id:
            raise HTTPException(status_code=400,detail="Product id already exists")
    products.append(product.dict())
    save_data(products)
    return product

@router.get("/products", response_model=List[Product])
def get_products(category: str = None, price: float = None):
    products = load_data()
    filtered_products = []
    for product in products:
        if category is not None:
            if product["category"] != category:
                continue
        if price is not None:
            if product["price"] > price:
                continue
        filtered_products.append(product)
    return filtered_products

@router.get("/products/{product_id}", response_model=Product)
def get_single_product(product_id: int):
    products = load_data()
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404,detail="Product not found")

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    products = load_data()
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product.name
            product["description"] = updated_product.description
            product["price"] = updated_product.price
            product["stock"] = updated_product.stock
            product["category"] = updated_product.category
            save_data(products)
            return product
    raise HTTPException(status_code=404,detail="Product not found")

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    products = load_data()
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_data(products)
            return {"message": "Product deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )