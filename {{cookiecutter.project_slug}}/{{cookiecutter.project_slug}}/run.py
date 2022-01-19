"""A test FastAPI application to reach a stable version for cookiecutter."""

import uvicorn
from core.config_parser import config
import core.env as environment

APP_ADDRESS = config['app']['app_address']
APP_PORT = int(config['app']['app_port'])

if __name__ == "__main__":# pragma: no cover
    if environment.LEVEL_OF_DEVELOPMENT == 'production':
        uvicorn.run("create_app:app", host=APP_ADDRESS,
                    port=APP_PORT, reload=False)
    else:
        uvicorn.run("create_app:app", host=APP_ADDRESS, port=APP_PORT,
                    reload=True, log_level="debug")
