"""
{{ cookiecutter.project_slug }}.

{{ cookiecutter.project_short_description }}.
"""

from fastapi import APIRouter

import {{ cookiecutter.project_slug }}.schemas.general as general_schema
from {{ cookiecutter.project_slug }}.core.config_parser import config

router = APIRouter()

APP_NAME = config['meta']['app_name']


@router.get('/', tags=["Home"],
            summary="Home Page",
            response_model=general_schema.Message,
            responses={
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
def home():
    """Return HomePage."""
    try:
        return {'msg': f'{APP_NAME} APIs is working. Use /docs or /redoc to see the documentation.'}

    except Exception as e:  # pragma: no cover
        return {'msg': f'Unexpected Error => {e}'}
