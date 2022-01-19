"""A test FastAPI application to reach a stable version for cookiecutter."""

from fastapi import APIRouter

import schemas.general as general_schema
from core.config_parser import config

router = APIRouter()

APP_NAME = config['meta']['app_name']


@router.get('/', tags=["Home"],
            summary="Home Page",
            response_model=general_schema.Message,
            responses={
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
def home():
    try:
        return {'msg': f'{APP_NAME} APIs is working. Use /docs or /redoc to see the documentation.'}

    except Exception as e:
        return {'msg': f'Unexpected Error => {e}'}
