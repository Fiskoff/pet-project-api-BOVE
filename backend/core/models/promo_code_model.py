import decimal
import datetime

from sqlalchemy import Integer, String, Numeric, Boolean, DateTime, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, validates

from core.models.base_model import BaseModel


class PromoCode(BaseModel):
    __tablename__ = 'promo_codes'

    __table_args__ = (
        CheckConstraint("LENGTH(promo_code) >= 4", name="chk_promo_code_length"),
        CheckConstraint("discount <= 50", name="chk_discount_max_50"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    promo_code: Mapped[str] = mapped_column(String(256))
    discount: Mapped[decimal.Decimal] = mapped_column(Numeric(4, 1))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    valid_from: Mapped[datetime.datetime] = mapped_column(DateTime)
    valid_to: Mapped[datetime.datetime] = mapped_column(DateTime)


    @validates('promo_code', 'discount')
    def validate_fields(self, key, value):
        if key == 'promo_code':
            if len(value) < 4:
                raise ValueError("Промокод должен содержать минимум 4 символа")
        elif key == 'discount':
            if value > 50:
                raise ValueError("Скидка не может быть больше 50%")
        return value

    def __str__(self):
        return f"Промокод: {self.promo_code}"