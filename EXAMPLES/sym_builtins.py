#!/usr/bin/env python
from sympy import Integer, Rational

a = Rational(2)  # <1>
b = Rational(10) # <1>

result = a**50/b**50  # <2>

print(result, type(result), '\n')  # <3>

x = Integer(1000)      # <4>
y = Integer(28000203)  # <4>

result = x * y  # <5>

print(result, type(result), '\n') # <6>

result = a * x  # <7>
print(result, type(result), '\n') # <8>
