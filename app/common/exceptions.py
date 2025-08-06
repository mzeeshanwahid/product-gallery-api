from fastapi import Request
from fastapi.responses import JSONResponse
import logging
import traceback

logger = logging.getLogger(__name__)

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error occurred: {exc}")
    traceback_str = ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(traceback_str)

    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error occurred. Please try again later.",
        },
    )
