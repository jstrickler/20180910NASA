#!/usr/bin/env python

import nasa

print(nasa, type(nasa))
print(dir(nasa))

print(nasa.jsc.eng)
print(dir(nasa.jsc.eng))

nasa.jsc.eng.nasautil.prep()

import pandas

print(dir(pandas))

import scipy

print(dir(scipy))
