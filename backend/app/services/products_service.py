import logging

from fastapi import HTTPException

from app.repositories.products_repository import ProductRepository
from core.models import Product, ProductVariant


logger = logging.getLogger(__name__)


class ProductService:
    @staticmethod
    async def get_all() -> list[Product]:
        products = await ProductRepository.get_all()
        return products


    @staticmethod
    async def get_by_id(product_id: int) -> Product:
        product_with_variants = await ProductRepository.get_by_id(product_id)
        if product_with_variants is None:
            logger.warning(f"GET /products/categories/{product_id} - status_code : 404")
            raise HTTPException(status_code=404, detail="Такого товара не существует")
        return product_with_variants


    @staticmethod
    async def get_variants_by_product_id(product_id: int) -> ProductVariant:
        variants = await ProductRepository.get_variants_by_product_id(product_id)
        if variants is None:
            logger.warning(f"GET /products/{product_id}/variants - status_code : 404")
            raise HTTPException(status_code=404, detail="Такого товара не существует")
        return variants

    @staticmethod
    async def get_new_products():
        new_products = await ProductRepository.get_new_products()
        if not new_products:
            logger.warning(f"GET /products/new - status_code : 404")
            raise HTTPException(status_code=404, detail="Новые товары отсутствуют")
        return new_products

    @staticmethod
    async def get_popular_products():
        popular_products = await ProductRepository.get_popular_products()
        if not popular_products:
            logger.warning(f"GET /products/popular - status_code : 404")
            raise HTTPException(status_code=404, detail="Популярные товары отсутствуют")
        return popular_products