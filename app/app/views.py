from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

router = APIRouter()


@router.get("/shippers/{shipper_id}", response_model=schemas.Shipper)
async def get_shipper(shipper_id: PositiveInt, db: Session = Depends(get_db)):
    db_shipper = crud.get_shipper(db, shipper_id)
    if db_shipper is None:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return db_shipper


@router.get("/shippers", response_model=List[schemas.Shipper])
async def get_shippers(db: Session = Depends(get_db)):
    return crud.get_shippers(db)


@router.get("/suppliers", response_model=List[schemas.Suppliers])
async def get_suppliers(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)


@router.get("/suppliers/{supp_id}")
async def get_supp(supp_id: PositiveInt, db: Session = Depends(get_db)):
    db_supp = crud.get_supplier(db, supp_id)
    if db_supp is None:
        raise HTTPException(status_code=404)
    return db_supp


@router.get("/suppliers/{supp_id}/products", response_model=List[schemas.Product])
async def get_products_by_supp(supp_id: PositiveInt, db: Session = Depends(get_db)):
    db_supp = crud.get_products_by_supp(db, supp_id)
    if db_supp is None or not db_supp:
        raise HTTPException(status_code=404)
    return [{'ProductID': product.ProductID, 'ProductName': product.ProductName, 'Category': {"CategoryID": product.CategoryID, 'CategoryName': product.CategoryName, }, 'Discontinued': product.Discontinued,} for product in db_supp]


@router.post("/suppliers", status_code=201)
async def create_supplier(supp: schemas.SupplierCreator, db: Session=Depends(get_db)):
    new_supp_id = crud.get_last_supp_id(db).SupplierID + 1
    return crud.add_supplier(supp_id=new_supp_id, db=db, supp=supp)


@router.put("/suppliers/{supp_id}", status_code=200)
async def update_supplier(supp_id: PositiveInt, supp: schemas.SupplierUpdater, db: Session=Depends(get_db)):
    db_supp = crud.get_suppliers(db)
    if supp_id not in [db_supplier.SupplierID for db_supplier in db_supp]:
        raise HTTPException(status_code=404)
    return crud.update_supplier(supp_id=supp_id, db=db, supp=supp)


@router.delete("/suppliers/{supp_id}", status_code=204)
async def delete_supplier(supp_id: PositiveInt, db: Session=Depends(get_db)):
    db_supp = crud.get_suppliers(db)
    if supp_id not in [db_supplier.SupplierID for db_supplier in db_supp]:
        raise HTTPException(status_code=404)
    return crud.delete_supplier(supp_id=supp_id, db=db)