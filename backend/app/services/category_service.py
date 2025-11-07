import logging

from app.repositories.categories_repository import ProductCategoryRepository
from core.models import ProductCategory

logger = logging.getLogger(__name__)


class ProductCategoryService:
    @staticmethod
    async def get_all() -> list[ProductCategory]:
        categories = await ProductCategoryRepository.get_all()
        return categories

    @staticmethod
    async def get_by_id(category_id: int) -> ProductCategory:
        category_with_products = await ProductCategoryRepository.get_by_id(category_id)
        return category_with_products