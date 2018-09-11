#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

lc = [f.upper() for f in fruits] # list comprehension
print(lc, '\n')

fg = (f.upper() for f in fruits)  # gen expression
print(fg, '\n')

g2 = (f[:3] for f in fg)


for fruit in g2:
    print(fruit)

