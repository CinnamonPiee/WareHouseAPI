from fastapi import APIRouter
from .product.views import router as products_router
from .order.views import router as order_router


router = APIRouter()


router.include_router(router=products_router, prefix="/products")
router.include_router(router=order_router, prefix="/orders")
