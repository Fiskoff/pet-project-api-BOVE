import decimal
from typing import List

from pydantic import BaseModel, Field, ConfigDict

from app.api.schemas import ProductVariantSchema


class ProductSchema(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор продукта", examples=[36])
    full_name: str = Field(..., description="Полное наименование товара", examples=["Жилетка"], max_length=256)
    article: str | None = Field(None, description="Артикул товара (может быть NULL)", examples=[None], max_length=256)
    price: decimal.Decimal = Field(..., description="Цена продукта", examples=[100.00], max_digits=10, decimal_places=2)
    description: str | None = Field(None, description="Описание товара (может быть NULL)", examples=["Описание товара"], max_length=16777215)
    composition_material: str = Field(..., description="Состав материала", examples=["78%пэ 20%виск 2%эл\nПодклад 75виск 25эл"], max_length=16777215)
    category_id: int = Field(..., description="ID связанной категории", examples=[11])

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)


class ProductByIdSchema(ProductSchema):
    variants: List[ProductVariantSchema] = Field(default_factory=list, description="Список вариантов товара")

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)


class GetProductsResponse(BaseModel):
    products: List[ProductSchema] = Field(..., description="Список всех товаров")


class GetProductByIdResponse(BaseModel):
    product: ProductByIdSchema = Field(..., description="Конкретный товар и его варианты")