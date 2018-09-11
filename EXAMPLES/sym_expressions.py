#!/usr/bin/env python
import sys
from sympy import Symbol, sin, pi, pprint

x = Symbol('x') # <1>
e1 = x + 1  # <2>
pprint(e1)
print()

y = Symbol('y')  # <1>
e2 = x - y + 17 + y - 16 + sin(pi)  # <3>
pprint(e2)
print()

pprint(e1 + e2)  # <4>
print()

pprint(e1 + e2 + 4 * x ** 2)  # <5>
print()

pprint(e1 ** 2)
