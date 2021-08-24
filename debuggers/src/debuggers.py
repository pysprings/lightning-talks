def fermat(n):
    """Returns triplets of the form x^n + y^n = z^n
    Warning! Untested with n > 2.
    """

    # source: "Fermat's last Python script"
    # https://earthboundkid.jottit.com/fermat.py
    for x in range(100):
        for y in range(1, x+1):
            for z in range(1, x**n+y**n + 1):
                if x**n + y**n == z**n:
                    yield x, y, z

for i in fermat(1):
    print(i)
