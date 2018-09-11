#!/usr/bin/env python
import numpy as np
import csv

with open('../DATA/columns_of_numbers.csv') as nums_in:
    rdr = csv.reader(nums_in)
    first_row = next(rdr)
    num_columns = len(first_row)


a = np.loadtxt(
    '../DATA/columns_of_numbers.csv',
    usecols=list(range(2, num_columns-1)),
    delimiter=',',
    skiprows=1,
)

print(a)
print(a.shape)
print(a.size)


