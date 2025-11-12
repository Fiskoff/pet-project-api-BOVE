import logging

from fastapi import APIRouter, Query, HTTPException
from starlette import status

from app.api.schemas import GetDiscountResponse
from app.services import PromoCodeService


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/promocode", tags=["Promo code"])


@router.get("", summary="Получить скидку по промо коду")
async def get_promo_code(
        promo_code: str = Query(..., min_length=4, description="Промокод", examples=["BOVE2025"])
) -> GetDiscountResponse:
    logger.info(f"GET /promocode")
    try:
        discount = await PromoCodeService.get_discount_by_promocode(promo_code)
        logger.info(f"GET /promocode - status_code : 200")
        return GetDiscountResponse(discount=discount)
    except HTTPException:
        raise
    except Exception as error:
        logger.error(f"GET /promocode - status_code : 500")
        logger.error(f"Error : {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении скидки"
        )