"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

import os

if 'DATA_DIRECTORY' in os.environ:
    if not os.path.isdir(os.environ['DATA_DIRECTORY']):
        os.mkdir(os.environ['DATA_DIRECTORY'])

SERVICE_NAMESPACE = ''
if 'service_namespace' in os.environ:  # pragma: no cover
    SERVICE_NAMESPACE = os.environ['service_namespace']
