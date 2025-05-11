import math

def is_tamgiac(a, b, c):
    if a + b > c or b + c > a or c + a > b:
        print('Is triangle')
    return True

def chuvitamgaic(a, b, c):
    return a + b + c

def s_tamgiac(a, b, c):
    p = chuvitamgaic(a, b, c) / 2
    S = 0
    if a > b > c:
        h = 2 * math.sqrt(p * (p + a) * (p + b) * (p + c)) / a
        S = 1 / 2 * h * a
    elif b > c > a:
        h = 2 * math.sqrt(p * (p + a) * (p + b) * (p + c)) / b
        S = 1 / 2 * h * b
    elif c > a > b:
        h = 2 * math.sqrt(p * (p + a) * (p + b) * (p + c)) / c
        S = 1 / 2 * h * c
    return S
