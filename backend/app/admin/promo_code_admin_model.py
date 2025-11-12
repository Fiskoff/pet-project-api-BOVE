from sqladmin import ModelView

from core.models import PromoCode


class PromoCodeAdmin(ModelView, model=PromoCode):
    name = "Промокод"
    name_plural = "Таблица промокодов"

    column_list = [
        PromoCode.id,
        PromoCode.promo_code,
        PromoCode.discount,
        PromoCode.is_active,
        PromoCode.valid_from,
        PromoCode.valid_to
    ]

    column_searchable_list = [
        PromoCode.promo_code,
    ]

    column_sortable_list = [
        PromoCode.id,
        PromoCode.promo_code,
        PromoCode.discount,
        PromoCode.is_active,
        PromoCode.valid_from,
        PromoCode.valid_to
    ]

    column_default_sort = [(PromoCode.id, True)]

    column_formatters = {
        PromoCode.is_active: lambda m, a: "Да" if m.is_active else "Нет",
    }

    column_labels = {
        PromoCode.id: "ID",
        PromoCode.promo_code: "Промокод",
        PromoCode.discount: "Скидка",
        PromoCode.is_active: "Активен?",
        PromoCode.valid_from: "Действительный с ",
        PromoCode.valid_to: "Действительный до"
    }

    form_columns = [
        PromoCode.promo_code,
        PromoCode.discount,
        PromoCode.is_active,
        PromoCode.valid_from,
        PromoCode.valid_to
    ]

    form_args = {
        "promo_code": {
            "label": "Промокод",
            "description": "Промокод должен состоять, минимум из четырёх символов",
        },
        "discount": {
            "label": "Скидка",
            "description": "Скидка не должна превышать 50%",
        },
        "is_active": {
            "label": "Промокод активен?",
        },
        "valid_from": {
            "label": "Действителен с",
        },
        "valid_to": {
            "label": "Действителен до",
        },
    }

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    page_size = 25
    page_size_options = [10, 25, 50, 100]