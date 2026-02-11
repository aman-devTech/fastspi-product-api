from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Product
from app.database import get_db
from app import crud


router = APIRouter()


@router.get("/product")
def get_all_products(db: Session = Depends(get_db)):
    return crud.get_all(db)


@router.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):

    db_product = crud.get_by_id(db, id)

    if not db_product:
        raise HTTPException(404, "Product not found")

    return db_product


@router.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):

    if product.price <= 0:
        raise HTTPException(400, "Price must be greater than zero")

    if product.quantity < 0:
        raise HTTPException(400, "Quantity cannot be negative")

    return crud.create(db, product)


@router.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):

    db_product = crud.get_by_id(db, id)

    if not db_product:
        raise HTTPException(404, "Product not found")

    if product.price <= 0:
        raise HTTPException(400, "Price must be greater than zero")

    if product.quantity < 0:
        raise HTTPException(400, "Quantity cannot be negative")

    return crud.update(db, db_product, product)


@router.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):

    db_product = crud.get_by_id(db, id)

    if not db_product:
        raise HTTPException(404, "Product not found")

    crud.delete(db, db_product)

    return {"message": "Product deleted successfully"}


@router.get("/product/search/{name}")
def search(name: str, db: Session = Depends(get_db)):
    return crud.search_by_name(db, name)


@router.get("/product/page/")
def get_by_page(page: int = 1, limit: int = 5, db: Session = Depends(get_db)):
    return crud.pagination(db, page, limit)


@router.get("/product/price/")
def price_filter(min_price: float, db: Session = Depends(get_db)):
    return crud.filter_by_price(db, min_price)