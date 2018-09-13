#!/usr/bin/env python
#
"""
Make an encoded binary puzzle to figure out
"""
from struct import Struct

puzzle_layout = 'fififhHfIdfdIiIh'


layout = Struct(puzzle_layout)

print(layout.size)

target = "Guido van Rossum"

target_ascii = target.encode() # [ord(c) for c in target]

print(target_ascii)

puzzle_data = layout.pack(*target_ascii)

print(puzzle_data)

PUZZLE_FILE = 'DATA/puzzle.data'

with open(PUZZLE_FILE, 'wb') as puzzle_out:
    puzzle_out.write(puzzle_data)

# now, to decode
with open(PUZZLE_FILE, 'rb') as puzzle_in:
    puzzle_data = puzzle_in.read()

    name_letters = [chr(int(x)) for x in layout.unpack(puzzle_data)]

    print(''.join(name_letters))
