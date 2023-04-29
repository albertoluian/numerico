from math import *
import copy
from time import sleep
a = [[4,-2, 0], [-2, 1, -1], [0, -1, -2],] # coeficientes do sistema linear
b = [0, 0, 5] # vetor resultante da equação
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
    e = 1
    x = [0, 0, 0] #chute do x aproximado
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
        print(e, x, xAnt)


print(convergencia())