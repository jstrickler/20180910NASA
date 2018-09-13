#!/usr/bin/env python

names = ['Bill', 'Bob', 'Mary', 'Sarah']
states = ['MO', "MA", 'MS', 'ME']

people = zip(names, states)

print(people)

print("First Try:")
for person in people:
    print(person)
print()

print("Second Try:")
for person in people:
    print(person)
print()

print(people)
