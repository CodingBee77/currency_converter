from fastapi import APIRouter

from api.routes import rates

router = APIRouter()
router.include_router(rates.router, tags=["rates"], prefix="/v1")
