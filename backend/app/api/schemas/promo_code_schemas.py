import decimal

from pydantic import BaseModel, Field


class PromoCodeSchema(BaseModel):
    promo_code: str = Field(..., min_length=4, description="Промокод", examples=["BOVE2025"])


class GetDiscountResponse(BaseModel):
    discount: decimal.Decimal = Field(..., description="Процент на который осуществляется скидка", examples=[15])
