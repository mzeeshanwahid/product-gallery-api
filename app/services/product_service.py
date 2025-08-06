from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, asc, desc
from app.models.product import Product

async def create_product(db: AsyncSession, product_data: dict):
    db_product = Product(**product_data)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10, filters: dict = {}):
    query = select(Product)

    if filters.get("category"):
        query = query.where(Product.category == filters["category"])
    if filters.get("min_price") is not None:
        query = query.where(Product.price >= filters["min_price"])
    if filters.get("max_price") is not None:
        query = query.where(Product.price <= filters["max_price"])
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
    if filters.get("min_price") is not None:
        query = query.where(Product.price >= filters["min_price"])
    if filters.get("max_price") is not None:
        query = query.where(Product.price <= filters["max_price"])
    if filters.get("search"):
        query = query.where(Product.title.ilike(f"%{filters['search']}%"))
        
    result = await db.execute(query)
    return result.scalar_one()
