import decimal
from typing import List

from pydantic import BaseModel, Field, ConfigDict

from core.models import SizeEnum


class ProductVariantSchema(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор варианта продукта", examples=[19])
    color: str = Field(..., description="Цвет варианта продукта", examples=["чёрный"], max_length=256)
    size: SizeEnum = Field(..., description="Размер варианта продукта", examples=["One Size"])
    quantity: int = Field(..., description="Количество на складе", examples=[15], ge=0)
    image: str = Field(..., description="Путь к изображению варианта", examples=["path/to/image.jpg"], max_length=16777215)
    price_variant: decimal.Decimal | None = Field(None, description="Цена конкретного варианта (Может быть NULL)", examples=[100.00], max_digits=10, decimal_places=2)
    product_id: int = Field(..., description="ID связанного продукта", examples=[36])

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)


class GetProductVariantsResponse(BaseModel):
    variants: List[ProductVariantSchema] = Field(..., description="Список вариантов конкретного продукта")