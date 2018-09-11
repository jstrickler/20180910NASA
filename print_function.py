#!/usr/bin/env python

x = 123.456
y = 'kitten'


print(x, y)

print(x, y, end='!')
print("OK")
print(x, y, end='!', sep="=>")
print(x, y, end='!', sep='')

with open("myfile.txt", "w") as my_out:
    print(x, y, end='!', sep="=>", file=my_out)
    print("A", file=my_out)
    print(x, y, end='!', sep='', file=my_out)
    print("B", file=my_out)


