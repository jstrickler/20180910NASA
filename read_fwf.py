#!/usr/bin/env python
from struct import Struct
from csv import writer

INPUT_FILE_NAME = 'sample100.por'
OUTPUT_FILE_NAME = 'converted.csv'

width = sum([2,9,9,12,12,12,12,12,12,12,12,12])
col=[1,2,4,6,7]
print("width:", width)
row_parser = Struct('2s9s9s12s12s12s12s12s12s12s12s12s')
print("size:", row_parser.size)
with open(INPUT_FILE_NAME, 'rb') as data_in:
    with open(OUTPUT_FILE_NAME, 'w') as data_out:
        wtr = writer(data_out)
        while True:
            record = data_in.read(width)
            if len(record) < width:
                break
            fields = [str(s) for s in row_parser.unpack(record)]
            wtr.writerow(fields)


