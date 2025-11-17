import decimal

from sqlalchemy import Integer, String, Text, ForeignKey, Numeric, Enum, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from core.models.base_model import BaseModel
from core.models.emun_models import SizeEnum


class ProductCategory(BaseModel):
    __tablename__ = 'product_categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(256))

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

    def __str__(self):
        return f"Категория: {self.name}"


class Product(BaseModel):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(256))
    article: Mapped[str | None] = mapped_column(String(256), nullable=True)
    price: Mapped[decimal.Decimal] = mapped_column(Numeric)
    new: Mapped[bool] = mapped_column(Boolean)
    popular: Mapped[bool] = mapped_column(Boolean)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    composition_material: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('product_categories.id'))

    category = relationship("ProductCategory", back_populates="products")
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")

    def __str__(self):
        return f"Товар: {self.full_name}"


class ProductVariant(BaseModel):
    __tablename__ = 'product_variants'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'))
    color: Mapped[str] = mapped_column(String(256))
    hex_color: Mapped[str] = mapped_column(String(256))
    size: Mapped[SizeEnum] = mapped_column(Enum(SizeEnum, name='size_enum'))
    quantity: Mapped[int] = mapped_column(Integer)
    image: Mapped[str] = mapped_column(Text)
    price_variant: Mapped[decimal.Decimal | None] = mapped_column(Numeric, nullable=True)

    product = relationship("Product", back_populates="variants")

    def __repr__(self):
        return f"Вариант ID: {self.id}"

