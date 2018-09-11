#!/usr/bin/env python

with open('DATA/presidents.txt') as potus_in:
    for line in potus_in:
        fields = line.rstrip().split(':')
        if fields[-1] == 'Whig':
            print(fields[2], fields[1])


