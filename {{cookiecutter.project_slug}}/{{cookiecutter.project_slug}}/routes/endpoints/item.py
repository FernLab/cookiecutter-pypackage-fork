"""A test FastAPI application to reach a stable version for cookiecutter."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config_parser import config
import core.env as environment

import schemas.general as general_schema
import schemas.item as item_schema

router = APIRouter()

APP_ADDRESS = environment.APP_DOMAIN
APP_PORT = int(config['app']['app_port'])
TAG = ['Test']

data = [
    {"id": "1", "price": 12.99},
    {"id": "2", "price": 15.89},
    {"id": "3", "price": 11.19},
    {"id": "4", "price": 13.49}
]


@router.get('/item', tags=TAG,
            summary="Get a list of items",
            response_model=item_schema.GETItemsResponse,
            responses={
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}}
            )
def get_items():
    """Returns a list of items."""

    try:
        return {"data": data}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"msg": f"Internal Server Error => {e}"})


@router.get('/item/{id}', tags=TAG,
            summary="Get item by id",
            response_model=item_schema.GETItemResponse,
            responses={
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}}
            )
def get_item_by_id(id: str):
    """Returns an item from list by its id."""

    try:
        item = [item for item in data if item["id"] == id]

        if not item:
            return JSONResponse(
                status_code=404,
                content={
                    "msg": f"Item with id ({id}) not found!"})

        return {"data": item}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"msg": f"Internal Server Error => {e}"})
