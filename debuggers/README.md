# Debugging with breakpoints

`breakpoint()` was introduced in [Python3.7](https://docs.python.org/3/library/functions.html?highlight=breakpoint#breakpoint).  Simply insert this function call anywhere you want to "break" execution and drop into a REPL.

You can control which debugger gets used by setting an environment variable like so:
```
export PYTHONBREAKPOINT=pdb.set_trace
```

You can also start your script in the debugging by calling the module directly:
```
python3 -m pdb debuggers.py
```

This allows you to debug code and you don't have to insert `breakpoint()` anywhere.

# pdb

https://docs.python.org/3/library/pdb.html#debugger-commands
https://realpython.com/python-debugging-pdb/


# ipdb
https://wangchuan.github.io/coding/2017/07/12/ipdb-cheat-sheet.html

    h(elp)
    w(here)
    d(own)
    u(p)
    b(reak): [ ([filename:]lineno | function) [, condition] ]
    tbreak: [ ([filename:]lineno | function) [, condition] ]
    cl(ear): [bpnumber [bpnumber ...] ]
    disable bpnumber: [bpnumber ...]
    enable bpnumber: [bpnumber ...]
    ignore bpnumber count
    condition bpnumber condition
    s(tep)
    n(ext)
    unt(il)
    r(eturn)
    run [args ...]
    c(ont(inue))
    l(ist): [first [,last]]
    a(rgs)
    p expression

# pudb
https://github.com/inducer/pudb
