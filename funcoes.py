import math
import numpy as np
def erro(y,y22):
    y = np.array(y)
    y22 = np.array(y22)
    yaux = [y[i]-y22[i] for i in range(len(y))]
    error = [i*i for i in yaux]
    error = np.array(error)
    print(yaux)
    return(np.sum(error))
def fx(i):
    return i
def fx2(i):
    return i*i
def fx3(i):
    return i*i*i
def fx4(i):
    return i*i*i*i
def fx5(i):
    return i*i*i*i*i
def fx6(i):
    return i*i*i*i*i*i
def f1(i):
    return 1
def sumfs(f, f2,vec):
    aux = 0.0
    for i in range(vec.__len__()):
        aux+=f(vec[i])*f2(vec[i])
    return aux
def sumys(f, y,vec):
    aux = 0.0
    for i in range(vec.__len__()):
        aux+=f(vec[i])*y[i]
    return aux

def formaAeb(funcoes, x, y):
    a = np.zeros(shape=(funcoes.__len__(), funcoes.__len__()), dtype=float)
    b = np.zeros(shape=(funcoes.__len__(), 1), dtype=float)
    print(b)
    for i in range(funcoes.__len__()):
        b[i][0] = sumys(funcoes[i], y, x)
        for j in range(funcoes.__len__()):
            a[i][j] = sumfs(funcoes[i], funcoes[j], x)
    return a, b