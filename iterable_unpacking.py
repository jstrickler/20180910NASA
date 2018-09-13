#!/usr/bin/env python

data = ['a', 'b', 'c']

i, j, k = data

data = ['a', 'b', 'c', 'd', 'e', 'f']

i, j, *k = data
print(i, j, k)

def spam(city, state, zip):
    print(city, state, zip)

c = "Houston"
s = "TX"
z = 77590

spam(c, s, z)

info = ['Durham', 'NC', 27705]
spam(*info)

# ham(**values)

# def ham(city, state, zip):  # required positional
def ham(*, city, state, zip):  # required named
        print(city, state, zip)

ham(city='Topeka', zip=30293, state="KS")

mydata = {'city':'Front Royal', 'state': 'VA', 'zip': 22630}

ham(**mydata)
