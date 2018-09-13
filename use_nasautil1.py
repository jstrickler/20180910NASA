#!/usr/bin/env python
import sys
from nasa.jsc.eng import nasautil

nasautil.prep()
nasautil.launch()
nasautil._monitor()

for path in sys.path:
    print(path)
