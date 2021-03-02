{% set group = cookiecutter.gitlab_group_or_username -%}
{% set subgroup = cookiecutter.gitlab_subgroup_name -%}
{% set slug = cookiecutter.project_slug -%}
{% if subgroup -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{subgroup}}/{{slug}}{%- endset -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{subgroup}}/{{slug}}.git{%- endset -%}
{% else -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{slug}}{%- endset -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{slug}}.git{%- endset -%}
{% endif -%}
.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at {{ projecturl }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitLab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitLab issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at {{ projecturl }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Commit Changes
--------------

How to
~~~~~~

1. Fork the `{{ cookiecutter.project_slug }}` repo on GitLab.
2. Clone your fork locally::

    $ git clone {{ giturl }}

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv {{ cookiecutter.project_slug }}
    $ cd {{ cookiecutter.project_slug }}/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ make lint
    $ python -m unittest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitLab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a merge request through the GitLab website.

Sign your commits
~~~~~~~~~~~~~~~~~

Please note that our license terms only allow signed commits.
A guideline how to sign your work can be found here: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

If you are using the PyCharm IDE, the `Commit changes` dialog has an option called `Sign-off commit` to
automatically sign your work.


License header
~~~~~~~~~~~~~~

If you commit new Python files, please note that they have to contain the following license header:

.. code:: bash

    # {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
    #
    # Copyright (C) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
    #
    # This software was developed within the context [...]


Merge Request Guidelines
------------------------

Before you submit a pull request, check that it meets these guidelines:

1. The merge request should include tests.
2. If the merge request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6, 3.7, 3.8 and 3.9. Check
   {{ projecturl }}/-/merge_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

{% if cookiecutter.use_pytest == 'y' -%}
    $ pytest tests.test_{{ cookiecutter.project_slug }}
{% else %}
    $ python -m unittest tests.test_{{ cookiecutter.project_slug }}
{%- endif %}
