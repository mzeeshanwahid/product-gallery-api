from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.database import AsyncSessionLocal
from app.services import product_service
from app.common.enums import ProductSortField, SortOrder

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

@router.get("/", summary="List products with pagination")
async def read_products(
    pageNo: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(10, ge=1, le=100, description="Page size"),
    sortField: Optional[ProductSortField] = Query(None),
    sortOrder: Optional[SortOrder] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    skip = (pageNo - 1) * pageSize

    filters = {
        "sortField": sortField,
        "sortOrder": sortOrder,
    }

    products: List[dict] = await product_service.get_products(db, skip=skip, limit=pageSize, filters=filters)
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
