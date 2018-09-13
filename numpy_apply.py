#!/usr/bin/env python

# Using a scipy function on a pandas DataFrame and returning as a DataFrame

import numpy as np
import pandas as pd
import scipy.signal as sps
import scipy
print(np.__version__, scipy.__version__, pd.__version__)

df1 = pd.DataFrame(np.random.rand(10, 3))

df2 = df1.apply(sps.resample, args=(6,))

print(type(df1), df1.shape)

print(type(df2), df2.shape)
