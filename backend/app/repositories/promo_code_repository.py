import decimal

from sqlalchemy import select

from core.db_helper import db_helper
from core.models import PromoCode


class PromoCodeRepository:
    @staticmethod
    async def get_discount_by_promocode(promo_code: str) -> decimal.Decimal | None:
        query = select(PromoCode.discount).where(PromoCode.promo_code == promo_code)
        async with db_helper.session_factory() as session:
            result = await session.execute(query)
            discount = result.scalar_one_or_none()
            return discount
