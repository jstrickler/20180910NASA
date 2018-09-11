#!/usr/bin/env python
import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle
import math

with open('saved_plot.fig', 'rb') as fig_in:
    saved_fig = pickle.load(fig_in)
    saved_fig.show()
