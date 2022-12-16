"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os
from pathlib import Path

if 'DATA_DIRECTORY' in os.environ:
    DATA_DIR = os.environ['DATA_DIRECTORY']
    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)
        print('\n')
        print('.=> The data directory was created for the first time.')
    else:
        print('\n')
        print('.=> The data directory already exists.')

    print('.=> Can be accessed by from {{ cookiecutter.project_slug }}.core.env import DATA_DIR')
    print(f'.=> PATH: {os.environ["DATA_DIRECTORY"]}')
    print('\n')

SERVICE_NAMESPACE = ''
if 'service_namespace' in os.environ:  # pragma: no cover
    SERVICE_NAMESPACE = os.environ['service_namespace']

    # In test mode (make pytest) the directory of the /data_dir will be created and managed
    # in /tests directory automatically.
    if os.environ['service_namespace'] == 'test-service':  # pragma: no cover
        DATA_DIR = os.path.join(os.getcwd(), 'tests', os.getenv('DATA_DIRECTORY'))
        if not os.path.isdir(DATA_DIR):
            Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
