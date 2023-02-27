"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os
from pathlib import Path

SERVICE_NAMESPACE = ''
if 'service_namespace' in os.environ:  # pragma: no cover
    SERVICE_NAMESPACE = os.environ['service_namespace']

    # In test mode (make pytest) the directory of the /data_dir will be created and managed
    # in /tests directory automatically.
    if os.environ['service_namespace'] == 'test-service':  # pragma: no cover
        DATA_DIR = os.path.join(os.getcwd(), 'tests', os.getenv('DATA_DIR'))
        if not os.path.isdir(DATA_DIR):
            Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

else:
    try:
        RESULTS_DIR = os.environ['DATA_DIR']
        if 'API_SERVER_SCOPE' in os.environ:
            if os.environ['API_SERVER_SCOPE'] == 'DEVELOPMENT':
                if not os.path.isdir(RESULTS_DIR):
                    try:
                        os.mkdir(RESULTS_DIR)
                    except Exception as e:
                        raise NotADirectoryError(f'Failed to create result directory => {e}')
    except Exception as e:
        print(f'Warning => Not defined <DATA_DIR> environment. => {e}')
