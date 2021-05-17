from sqlalchemy.orm import Session

from . import models


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
