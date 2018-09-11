#!/usr/bin/env python

from sympy import Symbol, var, symbols, pprint
from sympy.abc import x,y, theta  # <1>

k = Symbol('k')  # <2>
e1 = 2 * k + 1
pprint(e1)
print()

e2 = x * y * theta  # <3>
pprint(e2)
print()

(i,j) = symbols('a b')  # <4>
e3 = i**2 + j
pprint(e3)
print()

var('m n')  # <5>
e4 = 1/m**n
pprint(e4)
