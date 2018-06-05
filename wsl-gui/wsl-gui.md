---
# These slides were made to be presented by
# https://github.com/webpro/reveal-md

title: tkinter in WSL
revealOptions:
    transition: none
    touch: false

---

# GUI using WSL
<section style="text-align: left;">

Windows Subsystem for Linux:
*   allows Windows 10 users to run Linux distibutions *natively* in Windows (i.e. no VM).
*   Need certain version(s) of Windows 10
*   Can download different distros through the Microsoft Store
*   Supports all Python features supported by Linux

[Installing WSL Link](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

---

# Why WSL?
<section style="text-align: left;">

Linux has a lot of nice developer features that Windows
just doesn't have (e.g. `sed`, `awk`, etc).  `BASH` is also widely used, so you have lots of tutorials.

It's also *sometimes* easier to install things on Linux rather than Windows (e.g. compiled libraries w/o wheels).

---

# Why GUI
<section style="text-align: left;">
GUIs are nice for things like `matplotlib` and `Tkinter`.

These slides discuss one way to set this up.

---

# Install WSL
<section style="text-align: left;">

Easiest way is using the Microsft Store.

Google for other instructions.

---

# Set up Ubuntu
<section style="text-align: left;">

Install needed packages and update `pip`.


```bash
sudo apt-get update && sudo apt-get install x11-apps python-minimal python-tk python-pip
export PATH=~/.local/bin:$PATH
pip install --upgrade pip
pip install matplotlib
export DISPLAY=localhost:0.0
```

---

# Set up X11
<section style="text-align: left;">

Your Windows computer needs to be able to *render* the windows from your WSL command prompt.  To do this, you need to install some kind of X11 server.

For example: [xming](https://sourceforge.net/projects/xming)

Once it's installed, make sure it's running.

---

# Tkinter script
```python
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
```

---

# matplotlib script
```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.title('About as simple as it gets, folks')
plt.show()
```

---

# Questions?