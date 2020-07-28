#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script converts a Jinja2 template of YAML into proper YAML.

requirements:

    python -m pip install --upgrade pyyaml jinja2
"""

from pprint import pprint

import jinja2
import yaml

YAML_TEMPLATE = """
---

{% set base_path = 'teams' %}
{% set teamids = range(1, 5) %}
# team configuration###########################################################
{% for teamid in teamids %}
- team-name: Team-{{ "%02d" | format(teamid) }}
  base-port: {{ 5432 + teamid }}
  settings-path: {{ base_path }}/team-{{ "%02d" | format(teamid) }}
{% endfor %}
"""


JSON_TEMPLATE = """
---

{% set base_path = 'teams' %}
{% set teamids = range(1, 5) %}
[
{% for teamid in teamids %}
    {
        "team-name": "Team-{{ "%02d" | format(teamid) }}",
        "base-port": "{{ 5432 + teamid }}",
        "settings-path": "{{ base_path }}/team-{{ "%02d" | format(teamid) }}"
    }{{ "," if not loop.last -}}
{% endfor %}
]
"""


def render_template():
    template = jinja2.Template(YAML_TEMPLATE)
    return template.render()


def main():
    # First grab the rendered YAML as a string
    yaml_text = render_template()
    print("Here's the result of the template render:")
    print("<<<<<<")
    print(yaml_text)
    print(">>>>>>")

    # Convert that string into data (list in this case)
    yaml_data = yaml.safe_load(yaml_text)

    # now we get do things with the data.
    print()
    print("Here's the result of the YAML import:")
    print("<<<<<<")
    pprint(yaml_data)
    print(">>>>>>")


if __name__ == "__main__":
    main()
