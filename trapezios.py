from math import *
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
import copy

def f(x):
    return np.sqrt(1+x**3)
def f2(x):
    return 0
def f3(x):
    return 2
intervalo = [-4, 4]
dif = intervalo[1] - intervalo[0]
dx = dif/10000
integral = 0
xi = intervalo[0]
for i in range(10000):
        integral +=(f(xi)+f(xi+dx))*dx/2
        xi +=dx
print(integral, np.sqrt(np.pi))
print(f(0), f(1/2), f(1))
print((1/6)*(f(0) +4*f(1/2)+ f(1)))
x = np.linspace(-10, 100, 1000)
y = [f(i) for i in x]
plt.plot(x, y)
x = np.linspace(-10, 100, 1000)
y = [f2(i) for i in x]
plt.plot(x, y)
x = np.linspace(-10, 100, 1000)
y = [f3(i) for i in x]
plt.plot(x, y)
plt.show()