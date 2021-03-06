#!/usr/bin/env python
import pandas as pd
from printheader import print_header
import scipy as sp
from functools import partial
from scipy.signal import resample

cols = ['alpha','beta','gamma','delta','epsilon'] # <1>
index = ['a','b','c','d','e','f'] # <2>

values = [ # <3>
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]

df = pd.DataFrame(values, index=index, columns=cols)  # <4>

print(df)

def cube(x):
    return x ** 3

x = cube(df)

print(x)

print(type(x))

y = df.apply(resample, args=(3,), broadcast=True)
print(y)
print(type(y))

