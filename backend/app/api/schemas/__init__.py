from app.api.schemas.variants_schemas import (
    ProductVariantSchema,
    GetProductVariantsResponse,
    ColorVariantSchema
)
from app.api.schemas.products_schemas import (
    ProductSchema,
    ProductByIdSchema,
    GetProductsResponse,
    GetProductByIdResponse,
    GetProductsWithVariantsResponse,
    GetProductsColorsResponse
)
from app.api.schemas.categories_schemas import (
    ProductCategorySchema,
    ProductCategoryWithProductsSchema,
    GetCategoriesResponse,
    GetCategoryByIdResponse
)
from app.api.schemas.promo_code_schemas import (
    PromoCodeSchema,
    GetDiscountResponse
)