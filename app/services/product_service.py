from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product

async def create_product(db: AsyncSession, product_data: dict):
    db_product = Product(**product_data)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

