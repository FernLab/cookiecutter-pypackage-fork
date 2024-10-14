#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

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
{% elif cookiecutter.open_source_license == 'EUPL license' %}
# {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
#
# Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
#
# This software was developed within the context [...]
#
# This European Union Public License (the ‘EUPL’) applies to the Work (as defined
# below) which is provided under the terms of this License. Any use of the Work,
# other than as authorized under this License is prohibited (to the extent such
# use is covered by a right of the copyright holder of the Work).

# The Work is provided under the terms of this License when the Licensor (as
# defined below) has placed the following notice immediately following the
# copyright notice for the Work:
#
#         Licensed under the EUPL
#
# or has expressed by any other means his willingness to license under the EUPL.
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
{% elif cookiecutter.open_source_license == 'None' -%}

# {{ cookiecutter.project_name }}, {{ cookiecutter.project_short_description }}
#
# Copyright (c) {% now 'local', '%Y' %}  {{ cookiecutter.full_name }} (GFZ Potsdam, {{ cookiecutter.email }})
#
# This software was developed within the context [...]
#
# This program is not yet licensed and used for internal development only.
{% endif %}
{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else -%}
import unittest
{%- endif %}

<<<<<<< HEAD
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}  # noqa: F401 (imported but unused)
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}_cli
{%- endif %}

=======
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
>>>>>>> upstream/master
{%- if cookiecutter.use_pytest == 'y' %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
<<<<<<< HEAD
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke({{ cookiecutter.project_slug }}_cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}_cli.main' in result.output
    help_result = runner.invoke({{ cookiecutter.project_slug }}_cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}
=======
>>>>>>> upstream/master
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{%- endif %}
