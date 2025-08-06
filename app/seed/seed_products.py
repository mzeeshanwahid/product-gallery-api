import asyncio
import httpx
from app.database import AsyncSessionLocal, engine
from app.models.product import Product
from app.database import Base
from app.configs import THIRD_PARTY_PRODUCTS

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def fetch_and_seed_products():
    url = THIRD_PARTY_PRODUCTS
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    products = data.get("products", [])
    async with AsyncSessionLocal() as db:
        for prod in products:
            product = Product(
                id=prod["id"],
                title=prod["title"],
                description=prod.get("description"),
                category=prod.get("category"),
                price=prod.get("price"),
                rating=prod.get("rating"),
                brand=prod.get("brand"),
                availabilityStatus=prod.get("stock"),
                images=prod.get("images"),
                thumbnail=prod.get("thumbnail"),
            )
            await db.merge(product)
        await db.commit()

if __name__ == "__main__":
    asyncio.run(create_tables())
    asyncio.run(fetch_and_seed_products())
