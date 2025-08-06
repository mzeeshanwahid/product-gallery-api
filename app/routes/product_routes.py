from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal
from app.services import product_service
from typing import List

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

@router.get("/", summary="List products with pagination")
async def read_products(
    pageNo: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(10, ge=1, le=100, description="Page size"),
    db: AsyncSession = Depends(get_db)
):
    skip = (pageNo - 1) * pageSize

    products: List[dict] = await product_service.get_products(db, skip=skip, limit=pageSize)
    total_items: int = await product_service.count_products(db)
    total_pages = (total_items + pageSize - 1) // pageSize

    return {
        "data": products,
        "pagination": {
            "pageNo": pageNo,
            "pageSize": pageSize,
            "totalItems": total_items,
            "totalPages": total_pages
        }
    }
