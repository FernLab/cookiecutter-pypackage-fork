# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Unit test package for {{ cookiecutter.project_slug }}."""

import os
from dotenv import load_dotenv

from {{cookiecutter.project_slug}}.core.config_parser import config

# Load environments from .env file once we run the test functions.
load_dotenv()

os.environ['service_namespace'] = config['test']['service_namespace']
os.environ['DATA_DIR'] = os.getcwd()
