#!/usr/bin/env python

from sympy import Symbol, var, symbols, pprint
from sympy.abc import x,y, theta

k = Symbol('k')  # <1>
e1 = 2 * k + 1  # <2>
pprint(e1)  # <3>
print()

e2 = x * y * theta  # <4>
pprint(e2, use_unicode=True)  # <5>
print()

(i,j) = symbols('a b')  # <6>
e3 = i**2 + j  # <7>
pprint(e3)  # <8>
print()

var('m n')   # <9>
e4 = 1/m**n   # <10>
pprint(e4)  # <11>
