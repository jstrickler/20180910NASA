#!/usr/bin/env python


animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']
# dictionary comprehension
# list comp  [expr for var in iterable]

# dict comp {key:value for var in iterable}

d = {a.lower(): len(a) for a in animals} # <1>
print(d)

