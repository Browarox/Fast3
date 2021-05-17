from sqlalchemy.orm import Session

from . import models, schemas


def get_shippers(db: Session):
    return db.query(models.Shipper).all()


def get_shipper(db: Session, shipper_id: int):
    return (
        db.query(models.Shipper).filter(models.Shipper.ShipperID == shipper_id).first()
    )


def get_suppliers(db: Session):
    return db.query(models.Supplier).all()


def get_supplier(db: Session, supp_id: int):
    return (
        db.query(models.Supplier).filter(models.Supplier.SupplierID == supp_id).first()
    )

def get_products_by_supp(db: Session, supp_id: int):
    return db.query(models.Product.ProductID, models.Product.ProductName,models.Category.CategoryID,models.Category.CategoryName,models.Product.Discontinued).join(models.Category, models.Product.CategoryID == models.Category.CategoryID).filter(models.Product.SupplierID == supp_id).order_by(models.Product.ProductID.desc()).all()


def get_last_supp_id(db: Session):
    return db.query(models.Supplier.SupplierID).order_by(models.Supplier.SupplierID.desc()).first()

def add_supplier(supp_id: int, db: Session, supp: schemas.SupplierCreator):
    db_supp = models.Supplier(SupplierID=supp_id, CompanyName=supp.CompanyName, ContactName=supp.ContactName, ContactTitle=supp.ContactTitle, Address=supp.Address, City=supp.City, PostalCode=supp.PostalCode, Country=supp.Country, Phone=supp.Phone)
    db.add(db_supp)
    db.commit()
    db.refresh(db_supp)
    return db_supp