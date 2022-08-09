# os.path examples

Module documentation: https://docs.python.org/3/library/os.path.html

`os.path` is a functional way of dealing with operating systems paths.

Examples:
* `os.path.abspath('../../test.py')`
* `os.path.basename('../../test.py')`
* `os.path.splitext('test.py')`

You should use `os.path.pathsep` for platform compatibility (Linux and Windows), or use `os.path.join()`
```python
fname = "." + os.path.sep + "test.py"
# or
fname = os.path.join(".", "test.py")
```

# pathlib (introduced in Python 3.4)
Module documentation: https://docs.python.org/3/library/pathlib.html

`pathlib` provides an object-oriented way of dealing with operating system paths.

Examples:
* `Path("../../test.py").resolve()`
* `Path("../../test.py").name == "test.py"`

You don't have to worry about which "sep" to use, just use `/`:
```python
fname = Path(".") / "test.py"
# or
fname = Path(".", "test.py")
```

`Path.glob` takes a pattern and returns a generator!
```python
all_python_files = Path(".").glob("**/*.py")
print(all_python_files)
```

Also no need to use `open()`.  You can use the `Path` object directly.
```python
Path("myfile.md").write_text("# Here's a title!")
```

Here's a reference to how to move from `os.path` to `pathlib`:  
    https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module
