#!/usr/bin/env python
import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle
import math

x_values = range(1,51)
y_values = [math.cos(i) for i in x_values]

fig = plt.figure()

plt.plot(x_values, y_values)

with open('saved_plot.fig', 'wb') as fig_out:
    pickle.dump(fig, fig_out)
