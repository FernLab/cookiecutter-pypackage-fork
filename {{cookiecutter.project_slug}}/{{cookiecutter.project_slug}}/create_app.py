"""
{{ cookiecutter.project_slug }}.

{{ cookiecutter.project_short_description }}.
"""

from fastapi import FastAPI

from {{ cookiecutter.project_slug }}.core.config_parser import config
from {{ cookiecutter.project_slug }}.core import env as environment
from {{ cookiecutter.project_slug }}.routes.api import api_router

APP_NAME = config['meta']['app_name']
APP_DESC = config['meta']['app_description']
APP_VERSION = config['meta']['app_version']
APP_TERMS = config['meta']['app_terms']
APP_DOC_NAME = config['meta']['app_doc_name']

CONTACT_NAME = config['maintainer']['name']
CONTACT_LINK = config['maintainer']['link']
CONTACT_MAIL = config['maintainer']['mail']

LICENSE_NAME = config['license']['name']
# LICENSE_LINK = config['license']['link']

if environment.SERVICE_NAMESPACE:  # pragma: no cover
    service_namespace = environment.SERVICE_NAMESPACE
    fastapi_app = FastAPI(
        title=APP_NAME,
        description=APP_DESC,
        version=APP_VERSION,
        terms_of_service=APP_TERMS,
        contact={
            "name": CONTACT_NAME,
            "url": CONTACT_LINK,
            "email": CONTACT_MAIL,
        },
        license_info={
            "name": LICENSE_NAME,
            # "url": LICENSE_LINK
        },
        docs_url=f'/{service_namespace}/docs',
        redoc_url=f'/{service_namespace}/redoc',
        openapi_url=f'/{service_namespace}/{APP_DOC_NAME}.json')

    fastapi_app.include_router(api_router, prefix=f'/{service_namespace}')

else:
    fastapi_app = FastAPI(
        title=APP_NAME,
        description=APP_DESC,
        version=APP_VERSION,
        terms_of_service=APP_TERMS,
        contact={
            "name": CONTACT_NAME,
            "url": CONTACT_LINK,
            "email": CONTACT_MAIL,
        },
        license_info={
            "name": LICENSE_NAME,
            # "url": LICENSE_LINK
        }
    )
    fastapi_app.include_router(api_router)

app = fastapi_app
