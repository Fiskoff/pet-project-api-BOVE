import logging

from fastapi import APIRouter


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/categories", summary="Получить все категории товаров")
async def get_categories():
    pass


@router.get("/categories/{category_id}", summary="Получить конкретную категорию товара и её продукты")
async def get_category(category_id: int):
    pass


@router.get("", summary="Получить все продукты")
async def get_products():
    pass


@router.get("/{product_id}", summary="Получить конкретный продукт и его варианты")
async def get_product(product_id: int):
    pass


@router.get("/{product_id}/variants", summary="Получить все варианты конкретного продукта")
async def get_product_variants(product_id: int):
    pass