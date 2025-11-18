import logging

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.models import Product, ProductVariant
from core.db_helper import db_helper


logger = logging.getLogger(__name__)


class ProductRepository:
    @staticmethod
    async def get_all() -> list[Product]:
        async with db_helper.session_factory() as session:
            result = await session.execute(select(Product))
            products = result.scalars().all()
            return products


    @staticmethod
    async def get_by_id(product_id) -> Product | None:
        async with db_helper.session_factory() as session:
            result = await session.execute (
                select(Product)
                .options(selectinload(Product.variants))
                .where(Product.id == product_id)
            )
            product_with_variants = result.scalar_one_or_none()
            return product_with_variants


    @staticmethod
    async def get_variants_by_product_id(product_id: int) -> list[ProductVariant] | None:
        async with db_helper.session_factory() as session:
            chek_stmt = await session.execute(select(Product).where(Product.id == product_id))
            chek_product = chek_stmt.scalar_one_or_none()
            if chek_product is None:
                return None

            result = await session.execute (
                select(ProductVariant)
                .where(ProductVariant.product_id == product_id)
            )
            variants = result.scalars().all()
            return variants

    @staticmethod
    async def get_new_products() -> list[Product]:
        async with db_helper.session_factory() as session:
            result = await session.execute(
                select(Product)
                .options(selectinload(Product.variants))
                .where(Product.new == True)
            )
            products = result.scalars().all()
            return products

    @staticmethod
    async def get_popular_products() -> list[Product]:
        async with db_helper.session_factory() as session:
            result = await session.execute(
                select(Product)
                .options(selectinload(Product.variants))
                .where(Product.popular == True)
            )
            products = result.scalars().all()
            return products

    @staticmethod
    async def get_all_with_colors():
        async with db_helper.session_factory() as session:
            result = await session.execute(
                select(Product)
                .options(selectinload(Product.variants))
            )
            products = result.scalars().all()
            return products
