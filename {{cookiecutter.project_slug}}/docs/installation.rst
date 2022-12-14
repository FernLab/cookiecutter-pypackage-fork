{% set group = cookiecutter.gitlab_group_or_username -%}
{% set subgroup = cookiecutter.gitlab_subgroup_name -%}
{% set slug = cookiecutter.project_slug -%}
{% if subgroup -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{subgroup}}/{{slug}}.git{%- endset -%}
{% else -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{slug}}.git{%- endset -%}
{% endif -%}
.. _installation:

============
Installation
============


Using Mamba (recommended)
-------------------------

Using mamba_ (latest version recommended), {{ cookiecutter.project_name }} is installed as follows:


1. Create virtual environment for {{ cookiecutter.project_slug }} (optional but recommended):

   .. code-block:: bash

    $ mamba create -c conda-forge --name {{ cookiecutter.project_slug }} python=3
    $ mamba activate {{ cookiecutter.project_slug }}


2. Then clone the {{ cookiecutter.project_name }} source code and install {{ cookiecutter.project_name }} and all dependencies from the environment_{{ cookiecutter.project_slug }}.yml file:

   .. code-block:: bash

    $ git clone {{ giturl }}
    $ cd {{ cookiecutter.project_slug }}
    $ mamba env update -n {{ cookiecutter.project_slug }} -f tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml
    $ pip install .

Using Anaconda or Miniconda
---------------------------

Using conda_ (latest version recommended), {{ cookiecutter.project_name }} is installed as follows:


1. Create virtual environment for {{ cookiecutter.project_slug }} (optional but recommended):

   .. code-block:: bash

    $ conda create -c conda-forge --name {{ cookiecutter.project_slug }} python=3
    $ conda activate {{ cookiecutter.project_slug }}


2. Then clone the {{ cookiecutter.project_name }} source code and install {{ cookiecutter.project_name }} and all dependencies from the environment_{{ cookiecutter.project_slug }}.yml file:

   .. code-block:: bash

    $ git clone {{ giturl }}
    $ cd {{ cookiecutter.project_slug }}
    $ conda env update -n {{ cookiecutter.project_slug }} -f tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml
    $ pip install .


This is the preferred method to install {{ cookiecutter.project_name }}, as it always installs the most recent stable release and
automatically resolves all the dependencies.


Using pip (not recommended)
---------------------------

It is also possible to instal {{ cookiecutter.project_name }} via `pip`_. However, please note that {{ cookiecutter.project_name }} depends on some
open source packages that may cause problems when installed with pip. Therefore, we strongly recommend
to resolve the following dependencies before the pip installer is run:

    * TODO


Then, the pip installer can be run by:

   .. code-block:: bash

    $ pip install {{ giturl }}

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.



.. note::

    {{ cookiecutter.project_name }} has been tested with Python 3.6+., i.e., should be fully compatible to all Python versions from 3.6 onwards.


.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/
.. _conda: https://conda.io/docs
.. _mamba: https://github.com/mamba-org/mamba
