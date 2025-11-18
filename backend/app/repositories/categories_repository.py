import logging

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.models import ProductCategory
from core.db_helper import db_helper


logger = logging.getLogger(__name__)


class ProductCategoryRepository:
    @staticmethod
    async def get_all() -> list[ProductCategory]:
        async with db_helper.session_factory() as session:
            result = await session.execute(select(ProductCategory))
            categories = result.unique().scalars().all()
            return categories


    @staticmethod
    async def get_by_id(category_id) -> ProductCategory | None:
        async with db_helper.session_factory() as session:
            result = await session.execute (
                select(ProductCategory)
                .options(selectinload(ProductCategory.products))
                .where(ProductCategory.id == category_id)
            )
            category_with_products = result.scalar_one_or_none()
            return category_with_products
