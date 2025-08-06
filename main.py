from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.routes import product_routes
from app.configs import HOST, PORT, ENV, API_RATE_LIMIT
from app.common.exceptions import global_exception_handler

limiter = Limiter(key_func=get_remote_address, default_limits=[API_RATE_LIMIT])

app = FastAPI(
    title="Product Gallery API",
    description="API for managing products for gallery UI",
    version="1.0.0"
)

# Global exception handler
app.add_exception_handler(Exception, global_exception_handler) 

#Rate Limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SlowAPIMiddleware)

app.include_router(product_routes.router, prefix="/products", tags=["Products"])

reload = ENV != 'prod'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=reload)