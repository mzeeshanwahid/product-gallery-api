from fastapi import FastAPI

from app.configs import HOST, PORT, ENV

app = FastAPI(
    title="Product Gallery API",
    description="API for managing products for gallery UI",
    version="1.0.0"
)

reload = ENV != 'prod'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=reload)