from math import *
import copy
from time import sleep
import numpy as np
a = [[4,-2, -1, 0], [-2, 9, 0, -5],[-1, 0, 6, -3], [0, -5, -3, 10]] # coeficientes do sistema linear
b = [10, -5, 0, 0] # vetor resultante da equação
x = []
e = 1
def __round__(xis=list, decimals=int):
    xi = copy.deepcopy(xis)
    for i in range(xi.__len__()):
        xi[i] = round(xi[i], decimals)
    return xi
def convergencia():
    for i in range(b.__len__()):
        aii = abs(a[i][i])
        aji = 0
        for j in range(b.__len__()):
            if(j!=i):
                aji+=abs(a[i][j])
        print(aii, aji)
    return True
def gs():
    global x
    global e
    e = 1
    x = [0, 0, 0, 0] #chute do x aproximado
    xAnt = copy.deepcopy(x)
    while(e>=0.001):
        xAnt = copy.deepcopy(x)
        for i in range(x.__len__()):
            xi = 0
            for j in range(x.__len__()):
                if(i !=j):
                    xi += (-1)*a[i][j]*x[j]/a[i][i]
            xi += b[i]/a[i][i]
            x[i] = xi
        e = 0
        for i in range(x.__len__()):
            e+=(xAnt[i] - x[i])*(xAnt[i] - x[i])
        e = sqrt(e)
        print(round(e, 4), __round__(x, 4), __round__(xAnt, 4))


print(convergencia())
gs()
ar = np.array(a)
xis = np.array(x)
print(e, xis)
print(np.dot(ar, xis))
print(b)
