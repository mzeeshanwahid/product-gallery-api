from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.types import JSON
from app.database import Base
from pydantic import BaseModel
from typing import Optional, List, Any

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    category = Column(String)
    price = Column(Float)
    rating = Column(Float)
    brand = Column(String)
    availabilityStatus = Column(String)
    images = Column(JSON)
    thumbnail = Column(String)

class ProductReponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    price: float
    rating: Optional[float] = None
    brand: Optional[str] = None
    availabilityStatus: Optional[str] = None
    images: Optional[List[Any]] = None
    thumbnail: Optional[str] = None

    class Config:
        orm_mode = True

class Pagination(BaseModel):
    pageNo: int
    pageSize: int
    totalItems: int
    totalPages: int


class ProductListResponse(BaseModel):
    data: List[ProductReponse]
    pagination: Pagination
