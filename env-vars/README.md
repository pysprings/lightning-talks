# Environment Variables

## Intro

## The 12 Factor App
https://12factor.net

This is a set of recommendations for developing software-as-a-service solutions.  It's used to address concerns in security, maintenance, and deployability.

We're going to look at the _config_ part:

https://12factor.net/config
> III. Config  
> Store config in the environment  
> An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc).

Basically, any changes between environments should be reflected in environment variables because:

* It reduces logic within the application (think what happens when adding a new environment)
* Environment variables are supported by everything
* Environment variables are language-agnostic
* You'd have to try really hard to check them in to source code

However, there are some things you should know:

* It's pretty easy to show _all_ environment variables (e.g. `env`)
* Many people use a `.env` file anyway (example below)
* No way to update the variable once the process has been started (could be considered a good or bad thing)

## Python

## os
https://docs.python.org/3/library/os.html

```python
import os

PASSWORD = os.getenv("PASSWORD")
assert PASSWORD == "changeme"
```

You can use this after you have exported the environment variable to the process.  Some examples (assuming that script is called `env_test.py`):
```
PASSWORD=changeme python env_test.py
```
or:
```
export PASSWORD=changeme
python env_test.py
```

Notice, however, the password will be shown in your shell history.  Be careful!

## .env Files

Lots of us _cheat_ and use a file that never gets checked in to SCM.  The file is called `.env` by default.  This is basically a combination of storing configuration in environment variables and config files.

Why use `.env`?

* Far easier during development
* Keeps secrets out of shell history
* Largely supported (e.g. `docker` and `docker-compose`, language modules, etc)

https://pypi.org/project/python-dotenv/

In the example above, we might create a `.env` file that looks like this:
```
PASSWORD=changeme
```

We can then use something like `python-dotenv` to read it:
```
import os
from dotenv import load_dotenv
load_dotenv()

PASSWORD = os.getenv("PASSWORD")
assert PASSWORD == "changeme"
```

Notice that the bulk of the code did not change.  We're still reading variables from the _environment_.  `dotenv` takes the step of modifying the environment based on what it finds in the `.env` file.

Using a package like `dotenv` allow flexibility in how we develop with environment variables.  We can use either straight environment variables or `.env` files.

## Pydantic Settings

For a combination of settings management and environment variables, check out Pydantic Settings (and similiar packages):  
https://pydantic-docs.helpmanual.io/usage/settings/
