from fastapi import APIRouter
from project.crud import create_product,get_single_product, get_products,update_product,delete_product
from project.models import Product

router = APIRouter()

@router.post("/products")
def add_product(product: Product):
    return create_product(product.dict())

@router.get("/products")
def view_products():
    return get_products()

@router.get("/products/{product_id}")
def view_single_product(product_id: int):
    return get_single_product(product_id)

@router.put("/products/{product_id}")
def edit_product(product_id: int, product: Product):
    return update_product(product_id, product.dict())

@router.delete("/products/{product_id}")
def remove_product(product_id: int):
    return delete_product(product_id)