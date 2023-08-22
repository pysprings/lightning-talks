# singledispatch

`singledispatch` is Python's version of function "overloading" using [generic functions](https://docs.python.org/3/glossary.html#term-generic-function) (multiple functions implementing the same operation for different types). 

https://docs.python.org/3/library/functools.html#functools.singledispatch


This example uses the [geojson](https://geojson.readthedocs.io/en/latest/) library to convert geojson to WKT.

GeoJSON defines a few different objects.  In this module, we're only concerned with:
* Feature
* LineString
* Point
* Polygon

`WKT` (well known text) is another format for describing geography features.  It's a single string.

In this example, we create GeoJSON objects and convert them to their WKT equivalent.

The handy thing about `singledispatch` is that, as a user, you only need to import and call a single function.  Python will attempt to figure out the registered function to call based on the input types.

You can see a working example in `dispatch.py`.

## Alternative

Since functions are first-class objects in Python, you _could_ also do something like this:
```
def f_str(obj: str):
    ...
def f_int(obj: int):
    ...
def f_list(obj: list):
    ...

def do_a_thing(obj):
    type_map = {
        str: f_str,
        int: f_int,
        list: f_list
    }
    return type_map(type(obj), obj)
```

You can see a working example in `typemap.py`.
