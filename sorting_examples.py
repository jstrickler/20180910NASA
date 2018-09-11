#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print(n1, '\n')

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(item):
    return item.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def custom_sort(item):
    return len(item), item.lower()

f4 = sorted(fruits, key=custom_sort)
print("f4:", f4, '\n')

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

def by_last_name(person):
    return person[1], person[0]

p1 = sorted(people)
print("p1:", p1, '\n')

p2 = sorted(people, key=by_last_name)
print("p2:", p2, '\n')
print()

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
    'HOU': 'Houston Hobby',
}

print(airports.items())

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(item):
    return item[1], item[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()


for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0].lower())):
    print(abbr, name)
print()
