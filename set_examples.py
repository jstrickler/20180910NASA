#!/usr/bin/env python

john_countries = """Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split('\n')

clare_countries = """British Virgin Islands
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split('\n')

print(john_countries)
print(clare_countries)

john = set(john_countries)
clare = set(clare_countries)

print("Both:", john & clare)
print("Just one:", john ^ clare)
print("Either:", john | clare)
print("Just Clare:", clare - john)
print("Just John:", john - clare)

print("Kazakhstan" in john)
