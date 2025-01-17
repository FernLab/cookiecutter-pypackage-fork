.. SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
.. FileType: DOCUMENTATION
.. FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam



.. _usage:

Usage
=====

{% if cookiecutter.command_line_interface|lower == 'argparse' %}
Usage of the Python API
***********************
{% endif %}
To use {{ cookiecutter.project_name }} in a project::

    import {{ cookiecutter.project_slug }}

----
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}

Command line utilities
**********************

{{ cookiecutter.project_slug }}_cli.py
{% for _ in cookiecutter.project_slug %}-{% endfor %}-------

At the command line, {{ cookiecutter.project_name }} provides the **{{ cookiecutter.project_slug }}_cli.py** command:

.. argparse::
   :filename: ./../{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}_cli.py
   :func: get_argparser
   :prog: {{ cookiecutter.project_slug }}_cli.py
{%- endif %}
