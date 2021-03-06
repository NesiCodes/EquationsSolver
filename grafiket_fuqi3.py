import math

import matplotlib.pyplot as plt
import time
import numpy
import numpy as np


def plot_me(a, b, c, d, clr, mystr):
    if (a == 0 and b == 0):
        return np.array([f"x={(-d * 1.0) / c}"])

    elif (a == 0):

        D = c * c - 4.0 * b * d
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)

        x = numpy.arange(-4.0, 6.0, 0.05)
        y = [(a * i ** 3 + b * i ** 2 + c * i + d) for i in x]
        plt.plot(x, y, label='cubic', linestyle='-', color='r')
        plt.plot(x1, 0, 'k-o')
        plt.plot(x2, 0, 'k-o')
        plt.grid(True)
        plt.text(x1,-1.5,f"({round(x1)};{0})")
        plt.text(x2,-1.5,f"({round(x2)};{0})")
        plt.text(2, 4, "")
        plt.show(block=False)
        plt.pause(9000)
        plt.close()
        return -1

    f = findF(a, b, c)
    g = findG(a, b, c, d)
    h = findH(g, f)

    if f == 0 and g == 0 and h == 0:
        if (d / a) >= 0:
            x1 = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x1 = (-d / (1.0 * a)) ** (1 / 3.0)
        x = numpy.arange(-4.0, 6.0, 0.05)
        y = [(a * i ** 3 + b * i ** 2 + c * i + d) for i in x]
        plt.plot(x, y, label='cubic', linestyle='-', color='r')
        plt.plot(x1, 0, 'k-o')
        plt.plot(x1, 0, 'k-o')
        plt.plot(x1, 0, 'k-o')
        plt.text(x1,-1.5,f"({round(x1)};{0})")
        plt.grid(True)
        plt.text(2, 4, "")
        plt.show(block=False)
        plt.pause(9000)
        plt.close()
        return -1
        # return np.array([x, x, x])

    elif h <= 0:  # All 3 roots are Real

        i = math.sqrt(((g ** 2.0) / 4.0) - h)
        j = i ** (1 / 3.0)
        k = math.acos(-(g / (2 * i)))
        L = j * -1
        M = math.cos(k / 3.0)
        N = math.sqrt(3) * math.sin(k / 3.0)
        P = (b / (3.0 * a)) * -1

        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        x = numpy.arange(-4.0, 6.0, 0.05)
        y = [(a * i ** 3 + b * i ** 2 + c * i + d) for i in x]
        plt.plot(x, y, label='cubic', linestyle='-', color='r')
        plt.plot(x1, 0, 'k-o')
        plt.plot(x2, 0, 'k-o')
        plt.plot(x3, 0, 'k-o')
        plt.text(x1,-1.5,f"({round(x1)};{0})")
        plt.text(x2,-1.5,f"({round(x2)};{0})")
        plt.text(x3,-1.5,f"({round(x3)};{0})")
        plt.grid(True)
        plt.text(2, 4, "")
        plt.show(block=False)
        plt.pause(9000)
        plt.close()
        return -1

    elif h > 0:
        R = -(g / 2.0) + math.sqrt(h)
        if R >= 0:
            S = R ** (1 / 3.0)
        else:
            S = (-R) ** (1 / 3.0) * -1
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))
        else:
            U = ((-T) ** (1 / 3.0)) * -1

        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j

        x = numpy.arange(-4.0, 6.0, 0.05)
        y = [(a * i ** 3 + b * i ** 2 + c * i + d) for i in x]
        plt.plot(x, y, label='cubic', linestyle='-', color='r')
        plt.plot(x1, 0, 'k-o')
        plt.plot(x2, 0, 'k-o')
        plt.plot(x3, 0, 'k-o')
        plt.text(x1,-1.5,f"({round(x1)};{0})")
        plt.text(x2,-1.5,f"({round(x2)};{0})")
        plt.text(x3,-1.5,f"({round(x3)};{0})")
        plt.grid(True)
        plt.text(2, 4, "")
        plt.show(block=False)
        plt.pause(9000)
        plt.close()
        return -1


def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0



def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0


def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)

#(i) y = x**3
# plot_me(1, -6, 11, -6, 'r', 'y = x**3')

# plot_me(1,-23,142,-120, 'r' , 'yasddsa')

# #(ii) y = -x**3
# plot_me(-1, 0, 0, 0, 'r', 'y = -x**3')

# #(iii) y = x**3 - 4*x
# plot_me(1, 0, -4, 0, 'r', 'y = x**3 - 4*x')

# #(iv) y = -x**3 + 4*x
# plot_me(-1, 0, 4, 0, 'r', 'y = -x**3 + 4*x')

# #(v) y = x**3 -x + 8
# plot_me(1, 0, -1, 8, 'r', 'y = x**3 -x + 8')
#
# #(vi) y = -x**3 +x -8
# plot_me(-1, 0, 1, -8, 'r', 'y= -x**3 +x -8')