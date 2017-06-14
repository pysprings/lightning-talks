---
# These slides were made to be presented by
# https://github.com/webpro/reveal-md

title: pyinstaller
revealOptions:
    transition: none
    touch: false

---

# pyinstaller

> PyInstaller is a program that freezes (packages) Python programs
> into stand-alone executables, under Windows, Linux, Mac OS X, 
> FreeBSD, Solaris and AIX.

http://www.pyinstaller.org/

---

# Why?
<section style="text-align: left;">

*   Your audience may not need/want Python installed
*   Distribution *may* be easier than `pip install`
*   Built-in support for some packages (lxml, pygame, django, kivy, and many more)

---

# Why Not?
<section style="text-align: left;">

*   Output file size can be large (depends on your use)
*   Not cross-platform (Windows/Linux/OSX, 32bit/64bit)
*   No built-in cross-compiler
*   Too difficult to manage dependencies

---

# Example Build

```batch
pyinstaller --onefile --name prupload2 --paths ..
--version-file version.txt prupload2-cli.py
```

*   `onefile`: Create a one-file bundled executable
*   `name`: The name of the output file (w/o `.exe`)
*   `version-file`: Adds version info to the binary
*   `prupload2-cli.py`: The script used as the starting point

This created a 5MB binary for 140KB of Python

---

# Source Script
<section style="text-align: left;">
This is the entire source (w/o comments, of course) of  
`prupload2-cli.py`

```python
from prupload2 import main
if __name__ == '__main__':
    main()
```

---

# Example Output

<section style="text-align: left;">
```batch
> prupload2.exe --help
Performance Result Uploader 2 : version 1.2.1
usage: prupload2 [-h] -u USER -l [ID:FILE [ID:FILE ...]] -i IOTOOL [-s]
                [--csv] [--testdb] [--precon] [--component COMPONENT]
                [--noinst] [--nolat] [--force FORCE] [--drive] [--tag TAG]
                [--debug] [--trace] [-nu] [-nz]

optional arguments:
-h, --help            show this help message and exit
-u USER, --user USER  CQ User ID
...
```

Same as: `python prupload2-cli.py --help`, except you don't need Python or the `prupload2` package.

---

# Questions?

https://pyinstaller.readthedocs.io/en/stable/operating-mode.html