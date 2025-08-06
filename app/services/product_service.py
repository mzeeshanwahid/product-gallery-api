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

async def count_products(db: AsyncSession) -> int:
    query = select(func.count()).select_from(Product)
    result = await db.execute(query)
    return result.scalar_one()
