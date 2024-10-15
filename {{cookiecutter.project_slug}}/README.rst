{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% set group = cookiecutter.gitlab_group_or_username -%}
{% set subgroup = cookiecutter.gitlab_subgroup_name -%}
{% set slug = cookiecutter.project_slug -%}
{% if subgroup -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{subgroup}}/{{slug}}{%- endset -%}
    {%- set pagesurl -%}https://{{group}}.git-pages.gfz-potsdam.de/{{subgroup}}/{{slug}}{%- endset -%}
{% else -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{slug}}{%- endset -%}
    {%- set pagesurl -%}https://{{group}}.git-pages.gfz-potsdam.de/{{slug}}{%- endset -%}
{% endif -%}

{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: {{ pagesurl }}/doc/
{% endif %}


Status
------
.. image:: {{ projecturl }}/badges/main/pipeline.svg
        :target: {{ projecturl }}/pipelines
        :alt: Pipelines
.. image:: {{ projecturl }}/badges/main/coverage.svg
        :target: {{ pagesurl }}/coverage/
        :alt: Coverage
.. image:: https://img.shields.io/static/v1?label=Documentation&message=GitLab%20Pages&color=orange
        :target: {{ pagesurl }}/doc/
        :alt: Documentation
{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}

See also the latest coverage_ report and the pytest_ HTML report.


Feature overview
----------------

* TODO


History / Changelog
-------------------

You can find the protocol of recent changes in the {{ cookiecutter.project_name }} package
`here <{{ projecturl }}/-/blob/main/HISTORY.rst>`__.


Developed by
------------

.. image:: https://fernlab.gfz-potsdam.de/images/Fern.Lab_weiss-quadrat.png
        :target: https://fernlab.gfz-potsdam.de/
        :width: 10 %

{{ cookiecutter.project_slug }} has been developed by `FERN.Lab <https://fernlab.gfz-potsdam.de/>`_, the Helmholtz Innovation Lab "Remote sensing for sustainable use of resources", located at the `Helmholtz Centre Potsdam, GFZ German Research Centre for Geosciences <https://www.gfz-potsdam.de/en/>`_. FERN.Lab is funded by the `Initiative and Networking Fund of the Helmholtz Association <https://www.helmholtz.de/en/about-us/structure-and-governance/initiating-and-networking/>`_.


Credits
------------

This package was created with Cookiecutter_ and the `fernlab/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fernlab/cookiecutter-pypackage`: https://github.com/fernlab/cookiecutter-pypackage
.. _coverage: {{ pagesurl }}/coverage/
.. _pytest: {{ pagesurl }}/test_reports/report.html
