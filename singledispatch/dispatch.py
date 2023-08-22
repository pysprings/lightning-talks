#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for converting GeoJSON objects to WKT."""
from functools import singledispatch
from typing import Any

from geojson import Feature, LineString, Point, Polygon


# This is the default function
@singledispatch
def geojson_to_wkt(obj: Any) -> str:
    raise NotImplementedError(f"Object type '{type(obj)}' not implemented")


# We "register" all of our generic functions to the original generic function
@geojson_to_wkt.register
def _(obj: Point) -> str:
    # POINT(-73.96172712951027 40.787057297758196)
    geo_type = obj.type.upper()
    return geo_type + "(" + " ".join(str(x) for x in obj.coordinates) + ")"


@geojson_to_wkt.register
def _(obj: LineString) -> str:
    # LINESTRING(-73.96451294900065 40.78580462336586, -73.95857635550009 40.78792310301279)
    geo_type = obj.type.upper()
    coord_set_str = ", ".join([str(x[0]) + " " + str(x[1]) for x in obj.coordinates])
    return geo_type + "(" + coord_set_str + ")"


@geojson_to_wkt.register
def _(obj: Polygon) -> str:
    # POLYGON((-73.96388036116927 40.78659675844892, -73.96240837794453 40.785776990576466, ...
    geo_type = obj.type.upper()

    sets = []
    for coord_set in obj.coordinates:
        coord_set_str = ", ".join([str(x[0]) + " " + str(x[1]) for x in coord_set])
        sets.append("(" + coord_set_str + ")")

    return geo_type + "(" + ",".join(sets) + ")"


@geojson_to_wkt.register
def _(obj: Feature) -> str:
    geo_type = obj.geometry.type.upper()

    sets = []
    for coord_set in obj.geometry.coordinates:
        coord_set_str = ", ".join([str(x[0]) + " " + str(x[1]) for x in coord_set])
        sets.append("(" + coord_set_str + ")")

    return geo_type + "(" + ",".join(sets) + ")"


if __name__ == "__main__":
    point = Point((-115.81, 37.24))
    print("Default repr for Point type:")
    print("   ", point)
    print("...ask WKT:")
    print("   ", geojson_to_wkt(point))

    print()
    polygon = Polygon(
        [[(2.38, 57.322), (-120.43, 19.15), (23.194, -20.28), (2.38, 57.322)]]
    )
    print("Default repr for Polygon type:")
    print("   ", polygon)
    print("...ask WKT:")
    print("   ", geojson_to_wkt(polygon))
