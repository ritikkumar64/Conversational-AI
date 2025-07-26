import csv
from app.database import SessionLocal, engine, Base
from app.models import Product, Customer

Base.metadata.create_all(bind=engine)

def load_products():
    db = SessionLocal()
    with open("data/products.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.add(Product(name=row["name"], price=row["price"], category=row["category"]))
        db.commit()
    db.close()

def load_customers():
    db = SessionLocal()
    with open("data/customers.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.add(Customer(name=row["name"], email=row["email"]))
        db.commit()
    db.close()

if __name__ == "__main__":
    load_products()
    load_customers()
    print("Data Loaded Successfully")
