#!/usr/bin/env python

for i in range(10):
    print(i)
print()
print("i is", i)


fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

target = 'p'
for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print(target, "not found")
