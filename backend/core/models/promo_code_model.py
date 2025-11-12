import decimal
import datetime

from sqlalchemy import Integer, String, Numeric, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base_model import BaseModel


class PromoCode(BaseModel):
    __tablename__ = 'promo_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    promo_code: Mapped[str] = mapped_column(String(256))
    discount: Mapped[decimal.Decimal] = mapped_column(Numeric(3, 0))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    valid_from: Mapped[datetime.datetime] = mapped_column(DateTime)
    valid_to: Mapped[datetime.datetime] = mapped_column(DateTime)

    def __str__(self):
        return f"Промокод: {self.promo_code}"