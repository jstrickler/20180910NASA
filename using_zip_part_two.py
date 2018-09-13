#!/usr/bin/env python

names = ['Bill', 'Bob', 'Mary', 'Sarah']
states = ['MO', "MA", 'MS', 'ME']

people = zip(names, states)

print(people)

for person in people:
    print(person)
print()

# people = zip(names, states)

for name, state in zip(names, states):
    print(f"{name} is from {state}")

people = zip(names, states)

print(list(people))

my_dict = dict(zip(names, states))

print(my_dict)

print(list(my_dict.items()))

