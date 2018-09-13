#!/usr/bin/env python


def get_message():
    return "Hello, JSC world"


def display_message(message):
    print(message)

def spam(x, y=50, *z, name, file, **stuff):
    print(x)
    print(y)
    print(z)
    print(name)
    print(file)
    print(stuff)
    print()

spam(1, 2, name='Bob', file='wombats.txt')
spam(1, 2, 3, 'a', 'wombat', file='foo.bar', name='Jo')
spam(1, city='Austin', name='Justin', file='jsc.txt', color='red')


def ham(*, x_values, y_values):
    pass

ham(x_values=5, y_values=10)


def eggs(x, y, *z, **stuff):
    pass


def blah(foo, bar):
    print(foo, bar)

blah(5, 6)
blah(bar=8, foo=2)

def do_nothing(m):
    return m + 42

x = do_nothing(8)

print(x)






