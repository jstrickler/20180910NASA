#!/usr/bin/env python

d1 = dict()
d2 = {'a':5, 'b': 10, 'm': 99}
d3 = {}

print(len(d2))

print(d2['a'])
print(d2.get('x'))
print(d2.get('x', 'HUH'))

d4 = {'b': 5, 'o': 64, 'n': 36}

d2.update(d4)
print(d2, '\n')

def by_value(e):
    return e[1], e[0]

for letter, value in sorted(d2.items(), key=by_value):
    print(letter, value)
print()

print(d2.keys())
print(d2.values())

