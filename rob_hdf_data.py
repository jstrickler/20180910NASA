#!/usr/bin/env python
import numpy as np
import pandas as pd
import h5py

FILENAME = "sol_101_op2.h5"
KEY = "NASTRAN/INPUT/PROPERTY/PBUSH"

with h5py.File(FILENAME) as h5file:
    dataset = h5file[KEY]
    print("len(dataset:)", len(dataset))
    print("dataset:", dataset)
    print("dataset.dtype:", dataset.dtype)

    print("dataset[0]:", dataset[0])
    print("len(dataset[0]):", len(dataset[0]))
    field_names = dataset.dtype.fields.keys()
    print("field names:", field_names)

    print(dataset[0])
    d = dict(zip(field_names, dataset[0]))
    print("dict d", d)

    df = pd.DataFrame([list(dataset[0])], columns=dataset.dtype.fields.keys())
    print("dataframe df", df)
    print('-' * 60)
