import logging

from fastapi import HTTPException

from app.repositories.categories_repository import ProductCategoryRepository
from core.models import ProductCategory


logger = logging.getLogger(__name__)


class ProductCategoryService:
    @staticmethod
    async def get_all() -> list[ProductCategory]:
        categories = await ProductCategoryRepository.get_all()
        return categories

    @staticmethod
    async def get_by_id(category_id: int) -> ProductCategory | None:
        category_with_products = await ProductCategoryRepository.get_by_id(category_id)
        if category_with_products is None:
            logger.warning(f"GET /products/categories/{category_id} - status_code : 404")
            raise HTTPException(status_code=404, detail="Такой категории не существует")
        return category_with_products