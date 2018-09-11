#!/usr/bin/env python

cave_man = "Fred Flintstone"
city = 'Bedrock'

print(cave_man, "lives in", city)
#       0           1             0       1
print("{} lives in {}".format(cave_man, city))
print(f"{cave_man} lives in {city}")

print("{0} ({1}) lives in {1}".format(cave_man, city))

#   {3:...}   {:...}    printf("%d %s %.f")

result = 34.56 / 13.9
print(f"Result is {result:.2f}")

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

for first_name, last_name, product in people:
    print('{:^10s} {:^12s} {:^10.10}'.format(first_name, last_name, product))

big_num = 230_958_203_958_203_958_203_598
print("{:,d}".format(big_num))

x = 123_456.123_456

print(x)

data = [1, 2, 3]

print(f"{data[0]}")
print(f"{2 + 2}")
print(f"{data[0] * 10}")
