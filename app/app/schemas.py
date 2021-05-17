from pydantic import BaseModel, PositiveInt, constr
from typing import Optional


class Shipper(BaseModel):
    ShipperID: PositiveInt
    CompanyName: constr(max_length=40)
    Phone: constr(max_length=24)

    class Config:
        orm_mode = True


class Suppliers(BaseModel):
    SupplierID: PositiveInt
    CompanyName: constr(max_length=40)

    class Config:
        orm_mode = True


class Category(BaseModel):
    CategoryID: int
    CategoryName: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    ProductID: int
    ProductName: str
    Category: Optional[Category]
    Discontinued: int

    class Config:
        orm_mode = True

class SupplierCreator(BaseModel):
    CompanyName: str
    ContactName: Optional[str]
    ContactTitle: Optional[str]
    Address: Optional[str]
    City: Optional[str]
    PostalCode: Optional[str]
    Country: Optional[str]
    Phone: Optional[str]
