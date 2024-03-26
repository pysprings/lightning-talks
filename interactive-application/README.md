# Drop into an interactive shell during code execution

Sometimes it's handy to drop into an interactive shell when exploring your application.  There are a few ways to do this.


## stdlib

Python's standard library includes the `interact` method in the `code` module.

https://docs.python.org/3/library/code.html#code.interact

```python
from code import interact

interact()
```

Run the sample application with:
```shell
python -m stdlib_app -i
```

## IPython

IPython's `embed` method is a good alternative if you already use IPython for things.  IPython is nice for things like pretty-printing, history, tab completion, etc.

https://ipython.readthedocs.io/en/stable/interactive/reference.html#embedding

```python
from IPython import embed

embed()
```

Run the sample application with:
```shell
python -m ipython_app -i
```
