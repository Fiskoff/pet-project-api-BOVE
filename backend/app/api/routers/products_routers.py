import logging
from typing import Tuple

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.api.dependencies.pagination_dependecie import get_pagination
from app.api.schemas import GetDevicesResponse, GetDeviceByIdResponse
from app.services.products_service import DevicesService


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/devices", summary="Получить все девайсы с пагинацией")
async def get_devices(pagination: Tuple[int, int] = Depends(get_pagination)) -> GetDevicesResponse:
    skip, limit = pagination
    logger.info(f"GET /products/devices запрос: skip={skip}, limit={limit}")
    try:
        result = await DevicesService.get_devices(skip=skip, limit=limit)
        logger.info(f"GET /products/devices успешно: {len(result.devices)} девайсов возвращено")
        return result

    except ValueError as error:
        logger.warning(f"GET /products/devices ошибка клиента: {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    except Exception as error:
        logger.error(f"GET /products/devices внутренняя ошибка: {str(error)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении девайса"
        )


@router.get("/devices/{id}", summary="Получить девайс по id")
async def get_devices_by_id(devices_id: int) -> GetDeviceByIdResponse:
    logger.info(f"GET /products/devices/{devices_id} запрос")
    try:
        result = await DevicesService.get_device(devices_id)
        logger.info(f"GET /products/devices/{devices_id} успешно")
        return result

    except ValueError as error:
        if "не найден" in str(error).lower():
            logger.warning(f"GET /products/devices/{devices_id} девайс не найден")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Девайс не найден"
            )

        logger.warning(f"GET /products/devices/{devices_id} ошибка клиента: {str(error)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    except Exception as error:
        logger.error(f"GET /products/devices/{devices_id} внутренняя ошибка: {str(error)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера при получении девайса"
        )