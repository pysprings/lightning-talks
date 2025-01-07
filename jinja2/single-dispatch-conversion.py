#!/usr/bin/env python3
"""
TL;DR: Sometimes it's easier to convert template data using Python than
Jinja2 built-ins.

This is a sample script that shows how to use single-dispatch to convert
Python data types to Robot Framework syntax.

Example Robot Framework syntax:
    Array:
        1    2    3    4
        @{Empty}

    Dict:
        1=1    2=2    3=3    4=4
        &{Empty}

    Booleans:
        ${True}
"""
from jinja2 import Environment, BaseLoader
from functools import singledispatch

###############################################################################
# This first template uses pure-Jinja syntax to convert Python data types to
# Robot Framework syntax.  This is pretty clunky and we need lots of duplicate
# code.
###############################################################################
TEMPLATE1 = """
This is an array:
    {{ "    ".join(arr1) }}

This is a dictionary:
{% for key, value in dict1.items() %}
    ... {{ key }}={{ value }}
{%- endfor %}

This is a boolean True
    {{ "${True}" if bool1 else "${False}" }}

This is a boolean False
    {{ "${True}" if bool2 else "${False}" }}
"""
###############################################################################

###############################################################################
# This next template transfers all of the logic to a single-dispatch-enabled
# Python function.  This simplifies the template without making the Python
# code much more complex.
###############################################################################
TEMPLATE2 = '''
This is an array:
    {{ to_rf(arr1) }}

This is a dictionary:
    {{ to_rf(dict1) }}

This is a boolean
    {{ to_rf(bool1) }}
'''
###############################################################################

###############################################################################
# Single Dispatch functions to convert Python data types to Robot Framework
# syntax.
#
# Single Dispatch looks only at the first function parameter to determine
# which function to call and return.
###############################################################################
@singledispatch
def to_rf(value: str) -> str:
    if value:
        if str(value).lower() == "true":
            return "${True}"
        elif str(value).lower() == "false":
            return "${False}"
        elif str(value).lower() == "none":
            return "${None}"
        else:
            return value

    return "${None}"


@to_rf.register
def _(value: bool) -> str:
    if value:
        return "${True}"

    return "${False}"


@to_rf.register
def _(value: list) -> str:
    if value:
        return "    ".join([str(x) for x in value])

    return "@{EMPTY}"


@to_rf.register
def _(value: dict) -> str:
    if value:
        return "    ".join([f"{x}={y}" for x, y in value.items()])

    return "&{EMPTY}"
###############################################################################

def print_template(template_text: str, context: dict):
    env = Environment(loader=BaseLoader())

    # We can add Python callback functions to the environment globals.  These
    # will be called when the Jinja2 template is rendered.  The `to_rf` function
    # understands Python data types, so we only need one.  This simplifies the
    # template(s) so they don't need `to_rf_dict`, `to_rf_array`, etc.
    env.globals["to_rf"] = to_rf

    # Now just load and render the template.
    template = env.from_string(template_text)
    rendered_template = template.render(**context)
    print(rendered_template)


def main():

    # The "context" is the data we pass to the template for generation.
    context = {
        "arr1": ["1", "2", "3", "4"],
        "dict1": {"hello": "world", "test": "1"},
        "bool1": True,
        "bool2": False,
    }

    print("Complicated template without singledispatch")
    print()
    print_template(TEMPLATE1, context=context)

    print()
    print("Template with singledispatch")
    print()
    print_template(TEMPLATE2, context=context)

if __name__ == '__main__':
    main()
