import logging

from fastapi import APIRouter

from app.services import ProductCategoryService, ProductService
from app.api.schemas import GetCategoriesResponse, GetCategoryByIdResponse, GetProductsResponse, GetProductByIdResponse, GetProductVariantsResponse


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/categories", summary="Получить все категории товаров", response_model=GetCategoriesResponse)
async def get_categories():
    categories = await ProductCategoryService.get_all()
    return GetCategoriesResponse(categories=categories)


@router.get("/categories/{category_id}", summary="Получить конкретную категорию товара и её продукты", response_model=GetCategoryByIdResponse)
async def get_category(category_id: int):
    category_with_products = await ProductCategoryService.get_by_id(category_id)
    return GetCategoryByIdResponse(category=category_with_products)


@router.get("", summary="Получить все продукты", response_model=GetProductsResponse)
async def get_products():
    products = await ProductService.get_all()
    return GetProductsResponse(products=products)


@router.get("/{product_id}", summary="Получить конкретный продукт и его варианты", response_model=GetProductByIdResponse)
async def get_product(product_id: int):
    product_with_variants = await ProductService.get_by_id(product_id)
    return GetProductByIdResponse(product=product_with_variants)


@router.get("/{product_id}/variants", summary="Получить только варианты конкретного продукта", response_model=GetProductVariantsResponse)
async def get_product_variants(product_id: int):
    variants = await ProductService.get_variants_by_product_id(product_id)
    return GetProductVariantsResponse(variants=variants)