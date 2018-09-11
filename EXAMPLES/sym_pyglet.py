#!/usr/bin/env python
from sympy import Symbol, preview, Integral
# note: requires LaTex and dvipng

x = Symbol('x')

preview(x**2 + Integral(x**2, x) + 1/x)
