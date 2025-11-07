from typing import List

from pydantic import BaseModel, Field, ConfigDict

from app.api.schemas import ProductSchema


class ProductCategorySchema(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор категории", examples=[11])
    name: str = Field(..., description="Название категории", examples=["Жилетки"], max_length=256)

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)


class ProductCategoryWithProductsSchema(ProductCategorySchema):
    products: List[ProductSchema] = Field(default_factory=list, description="Список товаров в категории")

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)


class GetCategoriesResponse(BaseModel):
    categories: List[ProductCategorySchema] = Field(..., description="Список всех категорий")


class GetCategoryByIdResponse(BaseModel):
    category: ProductCategoryWithProductsSchema = Field(..., description="Конкретная категория и её товары")