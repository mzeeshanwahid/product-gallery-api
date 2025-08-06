from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import product_routes
from app.configs import HOST, PORT, ENV
from app.common.exceptions import global_exception_handler

app = FastAPI(
    title="Product Gallery API",
    description="API for managing products for gallery UI",
    version="1.0.0"
)

# Global exception handler
app.add_exception_handler(Exception, global_exception_handler) 

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes.router, prefix="/products", tags=["Products"])

reload = ENV != 'prod'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=reload)