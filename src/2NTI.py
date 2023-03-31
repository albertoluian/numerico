import math
def f1(x, r):
    return (x*x - r)
def flinha1(x):
    return 2*x


def q1(x, r):
    xa = x+1
    while(abs(x-xa)>0.0001):
        print(x)
        xa = x
        x = x - f1(x, r)/flinha1(x)
    print(x)

def f2(x):
    return (x-2)*(x-2)*(x-2)*(x-2)
def flinha2(x):
    return 4*(x-2)*(x-2)*(x-2)
def q2():
    x = 2.0002
    xa = x+1
    while(not abs(x-xa)<0.0001):
        print(x)
        xa = x
        x = x - f2(x)/flinha2(x)
    print(x)
def f3(x):
    return pow(math.e, x) - x*x
def flinha3(x):
    return pow(math.e, x) - 2*x
def q3():
    x = 0
    xa = x+1
    while(not abs(x-xa)<0.0001):
        print(x)
        xa = x
        x = x - f3(x)/flinha3(x)
    print(x)
def f4(x):
    return x*math.sin(x)
def flinha4(x):
    return math.sin(x) + x*math.cos(x)
def q4(x):
    xa = x+1
    while(not abs(x-xa)<0.0001):
        print(x)
        xa = x
        x = x - f4(x)/flinha4(x)
    print(x)
def f5c(x, r):
    return x*x*x - r
def flinha5c(x):
    return 3*x*x
def q5c(x, r):
    xa = x + 1   
    while(not abs(x-xa)<0.0001):
        print(x)
        xa = x
        x = x - f5c(x, r)/flinha5c(x)
    print(x)
print("q1\n")
q1(2, 7)
print("\nq2\n")
q2()
print("\nq3\n")
q3()
print("\nq4\n")
#forma numerica de calcular pi
#x1
q4(-3.14)
print("\n")
#x2
q4(3.14)
print("\n")
#x3
q4(0.001)
print("\nq5a\n")
q1(3, 8)
print("\nq5b\n")
q1(9, 91)
print("\nq5c\n")
q5c(2, 7)
print("\nq5d\n")
q5c(8, 200)

