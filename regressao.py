import numpy as np
import matplotlib.pyplot as plt
from funcoes import *
x = [1,2,3,4,5,6,7]
y = [2, 3.5, 6.5, 8, 9.4, 14, 18]
functions = [f1, np.exp, fx, fx2]
a, b = formaAeb(functions, x, y)
c = np.linalg.solve(a, b)
print(c)
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x5 = np.linspace(min(x), max(x), 1000)
y3 = []
index = -1
for i in x5:
    y3.append(0)
    index +=1
    for j in functions:
        y3[index] += c[functions.index(j)]*j(i)
plt.scatter(x,y)
plt.plot(x5,y3, 'r')
plt.show()

