import matplotlib.pyplot as plt
import time
import numpy

def plot_linear_eq(a, b):
    x = list(range(-10, 11))
    y = [ (a*i + b) for i in x]
    plt.plot(x, y, label='linear', linestyle='-', color='r')
    plt.grid()
    plt.show(block=False)
    plt.pause(9000)
    plt.close()

# y = ax + b generic linear equation
#
# (i) y = 0
# a = 6
# b = 9
# plot_linear_eq(a, b)
