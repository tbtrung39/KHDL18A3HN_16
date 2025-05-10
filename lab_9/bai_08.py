import math

def a(n):
    S = 0
    for i in range(1, n + 1):
        S += 1/(i *(i + 1))
    return S

def b(n):
    S = 0
    P = 1
    for i in range(1, n + 1):
        P *= i
        S += 1 + (1/P)
    return S

def c(n):
    if n == 3:
        S = math.sqrt(3)
        return S
    else:
        S = math.sqrt(3 * n + math.sqrt(3*(n - 1) + math.sqrt(n)))
        return S

def d(n):
    S = (n + (n - 1 + (3)**n)**n)**(1 + n)
    return S

n = int(input("Nhap n = "))
print(a(n))
print(b(n))
print(c(n))
print(d(n))