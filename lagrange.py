from itertools import product
from math import *
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
import copy
def f(x):
    return x*log(x) -3.2

# def lagrange(x, fx):                                                             
#     L = lambda num, xi: prod((num - xj) / (xi - xj) for xj in x if xj != xi)                                                                                   
#     return lambda num: sum([yi * L(num, xi) for xi, yi in zip(x, fx)])
#questao 1
# x = [1, 2, 3]
# y = [f(i) for i in x]
# print(y)
# poly = lagrange(x, y)
# poly2 = copy.deepcopy(poly)
# print(poly.roots)
# print(Polynomial(poly.coef[::-1]))
# print(poly(2.5), poly(10))
#questao 4
x = [100, 99.4 , 98.8 , 98.2 ]
x2 = copy.deepcopy(x)
y = [222.39, 222.30, 222.2, 222.13]
poly = lagrange(x, y)
print(Polynomial(poly.coef[::-1]))
print(poly(92), poly(95))
plt.plot(x, y)
x = np.linspace(95, 101, 1000)
y = [poly(i) for i in x]
plt.plot(x, y)
teste = [poly(i) for i in x2]
print(teste)
plt.show()