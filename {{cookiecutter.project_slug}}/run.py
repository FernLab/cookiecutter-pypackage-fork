"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}

It runs the service using `uvicorn.run`.

There are two ways to run the service:

1. Directly on the HOST machine by doing
```
mamba activate {{ cookiecutter.project_slug }}
python /path/to/the/file/run.py
```

2. Inside the docker container by doing
```
docker-compose -f /path/to/service_{{ cookiecutter.project_slug }}_dev.yaml up --build
```
in development mode and running on local machine and by doing
```
docker-compose -f /path/to/service_{{ cookiecutter.project_slug }}_dep.yaml up --build
```
in deployment mode if you want to run it on a remote machine say rz-vm1xx.gfz-potsdam.de machine.

To use the seconde option, a .env file should be created and set correctly.
"""

import os
import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    HOST = None
    PORT = None

    if 'API_SERVER_SCOPE' in os.environ:
        if os.environ['API_SERVER_SCOPE'] == 'deployment':
            print('\n')
            print('~.~.~.~.~.~.~.~.~.~.~.~ API RUNNING ~.~.~.~.~.~.~.~.~.~.~.~')
            print('~.~.~.~.~.~.~.~.~.~.~ PRODUCTION MODE ~.~.~.~.~.~.~.~.~.~.~')
            print('\n')

            try:
                HOST = os.environ['API_SERVER_HOST']
                PORT = int(os.environ['API_SERVER_PORT'])
            except:
                raise Exception(
                    'Undefined NEV => ENV <API_SERVER_HOST> and <API_SERVER_PORT> should be set.')

            if not HOST or not PORT:
                raise Exception(
                    'Undefined NEV => ENV <API_SERVER_HOST> and <API_SERVER_PORT> should be set.')

        else:
            raise Exception(
                'Undefined Scope => ENV <API_SERVER_SCOPE> should be set to <deployment>.')

    else:
        print('\n')
        print('~.~.~.~.~.~.~.~.~.~.~.~ API RUNNING ~.~.~.~.~.~.~.~.~.~.~.~')
        print('~.~.~.~.~.~.~.~.~.~.~ DEVELOPMENT MODE ~.~.~.~.~.~.~.~.~.~.~')
        print('\n')

        load_dotenv()

        HOST = os.getenv('API_SERVER_HOST')
        PORT = int(os.getenv('API_SERVER_PORT'))

        if not HOST or not PORT:
            HOST = '0.0.0.0'
            PORT = 4004

    os.environ['DATA_DIRECTORY'] = os.path.join(
        os.getcwd(), '{{ cookiecutter.project_slug }}', os.getenv('DATA_DIRECTORY'))

    uvicorn.run("{{ cookiecutter.project_slug }}.create_app:app",
                host=HOST, port=PORT, reload=True)
