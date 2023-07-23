# zipapp module

zipapp is a built-in Python module used to package up multiple modules/packages into a single "zip" file that's runnable by a Python interpreter.

This is super useful for sharing a set of modules as a single file, **as long as the user has Python installed**.

https://docs.python.org/3/library/zipapp.html
New in version 3.5.

Basic tutorial: https://realpython.com/python-zipapp/

## The application

Our example application is a very basic example that uses the requests library to send requests to jsontest.com to and log the output.

### Modules
* `logger.py`: a sample custom logger
* `app.py`: the main entrypoint

There's also a `JSON` filed called `urls.json` that has a list of URLs that our application will query.  This is to show the proper way to read files that are part of your Python application.

## Tricky bits

### Running the module
The application can be ran as a module with `python -m myapp`.  This makes the build structure very important to avoid Python errors like `No module named 'myapp'` and `attempted relative import with no known parent package`.

### Reading files

You can't use something like the `os` module to find/list/read files in your application once built with `zipapp`.  Your application no longer resides on the computer the same way it was before.  You have to use `importlib` to file and read them.

**!!ALWAYS USE importlib.resources TO READ FILES IN YOUR PACKAGE!!**
https://docs.python.org/3/library/importlib.resources.html

### The zipapp does not include Python itself!

This process only works if your intended audience has the correct version of Python already installed and available.  This is not a solution for shipping a self-contained executable.  That's a vastly more complex topic.

## Dealing with dependencies

You _probably_ want to include your dependencies in your `zipapp`.  One not-so-used feature of `pip` is the `--target` command-line argument.  You can tell `pip` where you want it to install the packages.  In this case, we want `pip` to install dependencies into our `./build` directory so `zipapp` will package them up.

!!Poetry can output a `requirements.txt` file through its `export` command-line option.!!

## Build Process
1. Copy the source into a "better" structure
2. Install required dependencies into the new structure
3. Build the "zipapp"

The `Makefile` provided with this repo has the following steps as:
```
	mkdir -p build
	cp -R myapp build
	python -m pip install -r requirements.txt --target build
	find ./build -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +
	mkdir -p dist
	python -m zipapp build -o dist/myapp.pyz -p "/usr/bin/env python3" -m "myapp.app:main"

```

You're left with the following folder structure in the build folder:
```
build
├── bin
├── certifi
├── certifi-2023.7.22.dist-info
├── charset_normalizer
├── charset_normalizer-3.2.0.dist-info
├── idna
├── idna-3.4.dist-info
├── myapp
├── requests
├── requests-2.31.0.dist-info
├── urllib3
└── urllib3-2.0.4.dist-info
```
