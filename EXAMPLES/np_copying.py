#!/usr/bin/env python
import numpy as np

a = np.array(
[[70, 31, 21, 76, 19, 5, 54, 66],
 [23, 29, 71, 12, 27, 74, 65, 73],
 [11, 84, 7, 10, 31, 50, 11, 98],
 [25, 13, 43, 1, 31, 52, 41, 90],
 [75, 37, 11, 62, 35, 76, 38, 4]]
) # <1>

print(a)
print()
print(id(a))

b = a

c = np.copy(a)

print(id(a), id(b), id(c))

d = a.T  # does transpose create a view

print(id(d))
print(a == d)

d[0][0] = 5
print(a)

a = a + 1000  # makes a copy!
a += 5  # does NOT make a copy
print(a)
print(id(a))
print(b)
