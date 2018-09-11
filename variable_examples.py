#!/usr/bin/env python

x = 10

print(x)
print(str(x))
print(repr(x))

movie_star = 'Billy Bob Thornton'

print(movie_star)
print(str(movie_star))
print(repr(movie_star))

x = 'wallaby'
y = x

x = 12.34

data = [1, 2, 3]
more_data = data
more_data.append(57)
print(data)
d2 = list(data)
d3 = data[:]

import copy
d4 = copy.deepcopy(data)



