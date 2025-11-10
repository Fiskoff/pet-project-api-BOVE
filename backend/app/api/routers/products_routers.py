import logging

from fastapi import APIRouter, HTTPException
from starlette import status

from app.services import ProductCategoryService, ProductService
from app.api.schemas import GetCategoriesResponse, GetCategoryByIdResponse, GetProductsResponse, GetProductByIdResponse, GetProductVariantsResponse


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/categories", summary="Получить все категории товаров")
async def get_categories() -> GetCategoriesResponse:
    logger.info(f"GET /products/categories")
    try:
        categories = await ProductCategoryService.get_all()
        logger.info(f"GET /products/categories - status_code : 200")
        return GetCategoriesResponse(categories=categories)
    except Exception as error:
        logger.error(f"GET /products/categories - status_code : 500")
        logger.error(f"Error : {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении категории"
        )


@router.get("/categories/{category_id}", summary="Получить конкретную категорию товара и её продукты")
async def get_category(category_id: int) -> GetCategoryByIdResponse:
    logger.info(f"GET /products/categories/{category_id}")
    try:
        category = await ProductCategoryService.get_by_id(category_id)
        logger.info(f"GET /products/categories/{category_id} - status_code: 200")
        return GetCategoryByIdResponse(category=category)
    except HTTPException:
        raise
    except Exception as error:
        logger.error(f"GET /products/categories - status_code: 500, error: {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении категории"
        )


@router.get("", summary="Получить все продукты")
async def get_products() -> GetProductsResponse:
    logger.info(f"GET /products")
    try:
        products = await ProductService.get_all()
        logger.info(f"GET /products - status_code : 200")
        return GetProductsResponse(products=products)
    except Exception as error:
        logger.error(f"GET /products - status_code : 500")
        logger.error(f"Error : {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении товаров"
        )


@router.get("/{product_id}", summary="Получить конкретный продукт и его варианты")
async def get_product(product_id: int) -> GetProductByIdResponse:
    logger.info(f"GET /{product_id}")
    try:
        product_with_variants = await ProductService.get_by_id(product_id)
        logger.info(f"GET /{product_id} - status_code : 200")
        return GetProductByIdResponse(product=product_with_variants)
    except HTTPException:
        raise
    except Exception as error:
        logger.error(f"GET /{product_id} - status_code : 500")
        logger.error(f"Error : {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении товара"
        )


@router.get("/{product_id}/variants", summary="Получить только варианты конкретного продукта")
async def get_product_variants(product_id: int) -> GetProductVariantsResponse:
    logger.info(f"GET /{product_id}/variants")
    try:
        variants = await ProductService.get_variants_by_product_id(product_id)
        logger.info(f"GET /{product_id}/variants - status_code : 200")
        return GetProductVariantsResponse(variants=variants)
    except HTTPException:
        raise
    except Exception as error:
        logger.error(f"GET /{product_id}/variants - status_code : 500")
        logger.error(f"Error : {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении вариаций по товару"
        )