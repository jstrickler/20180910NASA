#!/usr/bin/env python
from sympy import pi, Symbol, symbols, log, pprint

print(pi.evalf(50), '\n')  # <1>

x = Symbol('x')  # <2>
f = x ** (1 - log(log(log(log( 1 / x )))))  # <3>
pprint(f)

pprint(f.subs(x, pi).evalf())  # <4>
pprint(f.subs(x, 10).evalf())
pprint(f.subs(x, 3).evalf())
print()

a,b,c = symbols('a b c')  # <5>
exp = (a+b)*40-(c-a)/0.5  # <6>
pprint(exp)
pprint(exp.evalf(6,subs={a:6, b:5, c:2})) # <7>
