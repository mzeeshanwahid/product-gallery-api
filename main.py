from fastapi import FastAPI

from app.routes import product_routes
from app.configs import HOST, PORT, ENV

app = FastAPI(
    title="Product Gallery API",
    description="API for managing products for gallery UI",
    version="1.0.0"
)

app.include_router(product_routes.router, prefix="/products", tags=["Products"])

reload = ENV != 'prod'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=reload)