from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.types import JSON
from app.database import Base

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
