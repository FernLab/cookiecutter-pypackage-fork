import os

from core.config_parser import config

APP_DOMAIN = config['app']['app_address']

LEVEL_OF_DEVELOPMENT = ''
if 'level_of_development' in os.environ:
    LEVEL_OF_DEVELOPMENT = os.environ['level_of_development']
    APP_DOMAIN = 'localhost'

if 'server_name' in os.environ:
    APP_DOMAIN = os.environ['server_name']

SERVICE_NAMESPACE = ''
if 'service_namespace' in os.environ:
    SERVICE_NAMESPACE = os.environ['service_namespace']
