import numpy as np
import matplotlib.pyplot as plt
import math
import copy
from funcoes import *
x = [1,2,3,4,5,6,7]
y = [0.05,0.1,0.149, 0.159, 0.247, 0.296, 0.34]
x22 = copy.deepcopy(x)
y22 = copy.deepcopy(y)
y = [np.log(i) for i in y]
a, b = formaAeb([f1, fx], x, y)
c = np.linalg.solve(a, b)
print(a)
print("--------")
print(b)
print("solucao")
print(np.round(np.polyfit(x,y,1), 3), c)
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = copy.deepcopy(x22)
be = math.pow(math.e, c[0])
y = [be*math.pow(math.e, (c[1]*i)) for i in x]
print(x[4], c[1])
# y2 = [c[0]+i*c[1]+i*i*c[2]+i*i*i*c[3] for i in x]
# print("previsto")
print(math.pow(math.e, c[0])*math.pow(80, c[1]))
# plot the function
y3 = [-0.00565641*math.pow(math.e, -2.63688063*i) for i in x]
print(np.dot(a, c))
plt.plot(x,y, 'r')
plt.plot(x22,y22, 'r')
# show the plot
print("erro:")
print(erro(y, y22))
plt.show()

