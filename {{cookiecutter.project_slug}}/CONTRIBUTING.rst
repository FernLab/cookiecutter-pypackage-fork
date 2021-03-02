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

    {% if cookiecutter.open_source_license == 'MIT license' -%}
    # {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
    #
    # Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
    #
    # This software was developed within the context [...]
    #
    # Permission is hereby granted, free of charge, to any person obtaining a copy
    # of this software and associated documentation files (the "Software"), to deal
    # in the Software without restriction, including without limitation the rights
    # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    # copies of the Software, and to permit persons to whom the Software is
    # furnished to do so, subject to the following conditions:
    #
    # The above copyright notice and this permission notice shall be included in all
    # copies or substantial portions of the Software.
    #
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    # SOFTWARE.
    {% elif cookiecutter.open_source_license == 'BSD license' %}
    # {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
    #
    # Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
    # All rights reserved.
    #
    # This software was developed within the context [...]
    #
    # Redistribution and use in source and binary forms, with or without modification,
    # are permitted provided that the following conditions are met:
    #
    # * Redistributions of source code must retain the above copyright notice, this
    #   list of conditions and the following disclaimer.
    #
    # * Redistributions in binary form must reproduce the above copyright notice, this
    #   list of conditions and the following disclaimer in the documentation and/or
    #   other materials provided with the distribution.
    #
    # * Neither the name of the copyright holder nor the names of its
    #   contributors may be used to endorse or promote products derived from this
    #   software without specific prior written permission.
    #
    # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    # ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    # WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
    # IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
    # INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    # BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    # DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
    # OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
    # OF THE POSSIBILITY OF SUCH DAMAGE.
    {% elif cookiecutter.open_source_license == 'ISC license' -%}
    # {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
    #
    # Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
    #
    # This software was developed within the context [...]
    #
    # Permission to use, copy, modify, and/or distribute this software for any purpose
    # with or without fee is hereby granted, provided that the above copyright notice
    # and this permission notice appear in all copies.
    #
    # THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    # REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    # AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    # INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    # LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    # OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    # PERFORMANCE OF THIS SOFTWARE.
    {% elif cookiecutter.open_source_license == 'Apache Software License 2.0' -%}
    # {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
    #
    # Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
    #
    # This software was developed within the context [...]
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    # http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    {% elif cookiecutter.open_source_license == 'GNU General Public License v3' -%}
    # {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
    #
    # Copyright (c) {% now 'local', '%Y' %}  {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
    #
    # This software was developed within the context [...]
    #
    # This program is free software: you can redistribute it and/or modify it under
    # the terms of the GNU General Public License as published by the Free Software
    # Foundation, either version 3 of the License, or (at your option) any later
    # version.
    #
    # This program is distributed in the hope that it will be useful, but WITHOUT
    # ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
    # FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License along with
    # this program.  If not, see <http://www.gnu.org/licenses/>.
    {% endif %}

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
