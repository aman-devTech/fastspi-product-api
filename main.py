from fastapi import FastAPI,Depends, HTTPException
from models import Product
from database import session, engine
import database_model
from sqlalchemy.orm import Session

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "welcome to the world of tech :)"

# products = [
#     Product(id=1,name="phone",description= "budget phone",price =  699.99,quantity= 50),
#     Product(id=2,name="laptop",description= "powerful laptop",price =  999.99,quantity= 30),
#     Product(id=3,name="pen",description= "blue ink pen",price = 1.99,quantity= 100),
#     Product(id=4,name="table",description= "wodden table",price = 199.99,quantity= 20),
       
# ]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/product")
def get_all_products(db: Session = Depends(get_db)):
    
    db_products= db.query(database_model.Product).all()

    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product)\
                   .filter(database_model.Product.id == id)\
                   .first()

    if db_product:
        return db_product  

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

@app.post("/product")
def add_product(product : Product, db: Session = Depends(get_db)):
    if product.price <= 0:
        raise HTTPException(400, "Price must be greater than zero")
    
    if product.quantity < 0:
        raise HTTPException(400, "Quantity cannot be negative")
    
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    
    if product.price <= 0:
        raise HTTPException(400, "Price must be greater than zero")
    
    if product.quantity < 0:
        raise HTTPException(400, "Quantity cannot be negative")
    
    if db_product:
        db_product.name= product.name
        db_product.description= product.description
        db_product.price= product.price
        db_product.quantity= product.quantity
        db.commit()
        return db_product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return{"message":"Product deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Product not found")

# FEATURE-1 search product by name
@app.get("/product/search/{name}")
def search(name:str, db : Session = Depends(get_db)):

    result = db.query(database_model.Product).filter(database_model.Product.name.contains(name)).all()
    return result

# FEATURE-2 pagination
@app.get("/product/page/")
def get_by_page(page: int = 1,limit: int = 5, db: Session = Depends(get_db)):
    
    skip = (page - 1)* limit

    result = db.query(database_model.Product).offset(skip).limit(limit).all()

    return result

# FEATURE-3 price filter
@app.get("/product/price/")
def price_filter(min_price : float, db: Session = Depends(get_db)):

    result = db.query(database_model.Product).filter(database_model.Product.price >= min_price).all()

    return result