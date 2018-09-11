#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits] # list comprehension
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
floats = [float(n) for n in nums]
print("floats:", floats, '\n')

with open('DATA/mary.txt') as mary_in:
    lines = [line.rstrip() for line in mary_in]
print(lines, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

s = [(i, i**2, i**3) for i in range(1, 26)]
print(s)

suits = 'clubs diamonds hearts spades'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [(r, s) for s in suits for r in ranks]
print(cards, '\n')
