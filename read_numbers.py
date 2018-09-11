#!/usr/bin/env python


with open('DATA/columns_of_numbers.txt') as col_in:
    header = next(col_in)
    for raw_line in col_in:
        line = raw_line.rstrip()
        fields = line.split()
        print(fields)

