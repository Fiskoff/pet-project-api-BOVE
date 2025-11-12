import logging
import decimal

from fastapi import HTTPException

from app.repositories.promo_code_repository import PromoCodeRepository


logger = logging.getLogger(__name__)


class PromoCodeService:

    @staticmethod
    async def get_discount_by_promocode(promo_code: str) -> decimal.Decimal:
        discount = await PromoCodeRepository.get_discount_by_promocode(promo_code)
        if discount is None:
            logger.warning(f"GET /promocode - status_code : 404")
            raise HTTPException(status_code=404, detail="Такого промокода не существует")
        return discount