#!/usr/bin/env python
from sympy import Derivative, sin, pprint
from sympy.abc import x, y  # <1>

e = Derivative(sin(x), x, y)  # <2>
pprint(e)
print()

pprint(e._args)  # <3>
