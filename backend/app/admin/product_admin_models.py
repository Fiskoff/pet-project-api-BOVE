from sqladmin import ModelView

from core.models import Product, ProductCategory, ProductVariant


class ProductCategoryAdmin(ModelView, model=ProductCategory):
    name = "категория"
    name_plural = "Таблица категорий"

    column_list = [
        ProductCategory.id,
        ProductCategory.name,

        ProductCategory.products
    ]

    column_searchable_list = [
        ProductCategory.id,
        ProductCategory.name
    ]

    column_sortable_list = [
        ProductCategory.id,
        ProductCategory.name
    ]

    column_labels = {
        ProductCategory.id: "ID",
        ProductCategory.name: "Название",
    }

    form_columns = [
        ProductCategory.name,
    ]

    form_args = {
        "name": {
            "label": "Название категории",
        },
    }

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    page_size = 25
    page_size_options = [10, 25, 50, 100]


class ProductAdmin(ModelView, model=Product):
    name = "товар"
    name_plural = "Таблица товаров"

    column_list = [
        Product.id,
        Product.full_name,
        Product.article,
        Product.price,
        Product.description,

        Product.category,
        Product.variants,
    ]

    column_searchable_list = [
        Product.id,
        Product.full_name,
        Product.article,
        Product.description,
        Product.price,
    ]

    column_sortable_list = [
        Product.id,
        Product.full_name,
        Product.article,
        Product.price,
    ]

    column_default_sort = [(Product.id, True)]

    column_formatters = {
        Product.article: lambda m, a: "Н/Д" if m.article is None else m.article,
        Product.description: lambda m, a: "Н/Д" if m.description is None else m.description,
    }

    column_labels = {
        Product.id: "ID",
        Product.full_name: "Название",
        Product.article: "Артикул",
        Product.price: "Цена",
        Product.description: "Описание товара",
        Product.composition_material: "Материал",
        Product.category_id: "Категория",

        Product.category: "Категория",
        Product.variants: "Варианты",
    }

    form_columns = [
        Product.full_name,
        Product.article,
        Product.price,
        Product.description,
        Product.composition_material,
        Product.category,
    ]

    form_args = {
        "full_name": {
            "label": "Название товара",
        },
        "article": {
            "label": "Артикул товара",
            "description": "Может быть не указан",
        },
        "price": {
            "label": "Цена",
        },
        "description": {
            "label": "Описание товара",
            "description": "Может быть не указано",
        },
        "composition_material": {
            "label": "Состав",
        },
        "category_id": {
            "label": "Id категории",
        },
    }

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    page_size = 25
    page_size_options = [10, 25, 50, 100]


class ProductVariantAdmin(ModelView, model=ProductVariant):
    name = "вариант товара"
    name_plural = "Таблица вариантов товара"

    column_list = [
        ProductVariant.id,
        ProductVariant.color,
        ProductVariant.size,
        ProductVariant.quantity,
        ProductVariant.image,
        ProductVariant.price_variant,

        ProductVariant.product
    ]

    column_searchable_list = [
        ProductVariant.id,
        ProductVariant.color,
        ProductVariant.size,

    ]

    column_sortable_list = [
        ProductVariant.id,
        ProductVariant.color,
        ProductVariant.size,
        ProductVariant.quantity,
        ProductVariant.price_variant,

    ]

    column_default_sort = [(Product.id, True)]

    column_formatters = {
        ProductVariant.price_variant: lambda m, a: "Н/Д" if m.price_variant is None else m.price_variant,
    }

    column_labels = {
        ProductVariant.id: "ID",
        ProductVariant.color: "Цвет",
        ProductVariant.size: "Размер",
        ProductVariant.quantity: "Количество",
        ProductVariant.image: "Изображение",
        ProductVariant.price_variant: "Цена",

        ProductVariant.product: "Товар",
    }

    form_columns = [
        ProductVariant.color,
        ProductVariant.size,
        ProductVariant.quantity,
        ProductVariant.image,
        ProductVariant.price_variant,
        ProductVariant.product
    ]

    form_args = {
        "color": {
            "label": "Цвет товара",
        },
        "size": {
            "label": "Размер товара",
            "description": "Выберите размер",
        },
        "quantity": {
            "label": "Количество",
        },
        "image": {
            "label": "Изображение",
        },
        "price_variant": {
            "label": "Цена конкретного варианта",
            "description": "Может быть не указана",
        },
        "product_id": {
            "label": "Id товара",
        },
    }

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    page_size = 25
    page_size_options = [10, 25, 50, 100]





