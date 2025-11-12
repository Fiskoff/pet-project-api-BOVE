from app.api.routers.products_routers import router as product_router
from app.api.routers.promo_code_router import router as promo_code_router


routers = [
    product_router, promo_code_router
]