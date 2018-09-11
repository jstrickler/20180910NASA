#!/usr/bin/env python

import re

with open("../DATA/parrot.txt") as mary_in:
    s = {w.lower() for ln in mary_in  for w in re.split(r'\W+', ln) if w} #<1>
print(s)
