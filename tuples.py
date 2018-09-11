#!/usr/bin/env python


person = 'Jennifer', 'Wood', 32

print(len(person))
print(person)
print(person[0], person[1])

first_name, last_name, age = person
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook', "wombats", "dope"),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'Git'),
    ('Billy Bob', 'Thornton'),
]
print(people[0])
print(people[0][0])
print(people[0][0][0])
print()


# for x in ITERABLE:
for first_name, last_name, *_ in people:
# for person in people:
    # first_name, last_name, product = next(people)
    # person = next(people)
    print(first_name, last_name)
print('-' * 60)


values = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

w, x, *y, z = values
print(w, x, y, z)
