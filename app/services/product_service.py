from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, asc, desc
from app.models.product import Product
from fastapi import HTTPException

async def create_product(db: AsyncSession, product_data: dict):
    db_product = Product(**product_data)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10, filters: dict = {}): 
    # minPrice = filters.get("minPrice") is not None
    # maxPrice = filters.get("maxPrice") is not None

    # if minPrice is not None and maxPrice is not None and minPrice > maxPrice:
    #     raise HTTPException(status_code=400, detail="minPrice cannot be greater than maxPrice")

    query = select(Product)

    if filters.get("category"):
        query = query.where(Product.category == filters["category"])
    if filters.get("minPrice") is not None:
        query = query.where(Product.price >= filters["minPrice"])
    if filters.get("maxPrice") is not None:
        query = query.where(Product.price <= filters["maxPrice"])
    if filters.get("search"):
        query = query.where(Product.title.ilike(f"%{filters['search']}%"))

    sort_field = filters.get("sortField")
    sort_order = filters.get("sortOrder", "ASC")

    if sort_field:
        column = getattr(Product, sort_field.value)
        if sort_order == "DESC":
            query = query.order_by(desc(column))
        else:
            query = query.order_by(asc(column))
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def count_products(db: AsyncSession, filters: dict = {}) -> int:
    query = select(func.count()).select_from(Product)

    if filters.get("category"):
        query = query.where(Product.category == filters["category"])
    if filters.get("minPrice") is not None:
        query = query.where(Product.price >= filters["minPrice"])
    if filters.get("maxPrice") is not None:
        query = query.where(Product.price <= filters["maxPrice"])
    if filters.get("search"):
        query = query.where(Product.title.ilike(f"%{filters['search']}%"))
        
    result = await db.execute(query)
    return result.scalar_one()
