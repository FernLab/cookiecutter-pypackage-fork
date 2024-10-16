import re
import sys
from datetime import datetime

# Regex for validating Python module names
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

# The project slug to validate
module_name = '{{ cookiecutter.project_slug }}'

# Check if the module name is valid
if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. '
          'Please do not use a - and use _ instead' % module_name)
    # Exit to cancel project
    sys.exit(1)

# Fetch the current year and add it to the context
current_year = datetime.now().year

# Define a mapping of license names to SPDX identifiers
license_mapping = {
    "MIT license": "MIT",
    "BSD license": "BSD-3-Clause",
    "ISC license": "ISC",
    "Apache Software License 2.0": "Apache-2.0",
    "GNU General Public License v3": "GPL-3.0-or-later",
    "EUPL license": "EUPL-1.2",
    "None": "NOASSERTION"  # For no license
}

# Get the selected license from cookiecutter context
selected_license = '{{ cookiecutter.open_source_license }}'

# Map the selected license to the corresponding SPDX identifier
spdx_identifier = license_mapping.get(selected_license, "NOASSERTION")

# Add the current year and SPDX identifier to the cookiecutter context
cookiecutter_context = {
    "year": current_year,
    "spdx_license": spdx_identifier
}
