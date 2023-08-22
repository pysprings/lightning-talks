#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f_str(obj: str):
    print("Doing something with a string")


def f_int(obj: int):
    print("Doing something with an int")


def f_list(obj: list):
    print("Doing something with a list")


def do_a_thing(obj):
    type_map = {str: f_str, int: f_int, list: f_list}

    func = type_map.get(type(obj))

    if not func:
        raise TypeError(f"Unknown type: {type(obj)}")

    return func(obj)  # type: ignore


if __name__ == "__main__":
    do_a_thing("my string")
    do_a_thing(1)
    do_a_thing([1, 2, 3])

    # undefined type of dict
    do_a_thing({1: 1})
