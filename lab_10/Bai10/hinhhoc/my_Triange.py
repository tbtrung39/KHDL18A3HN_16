import math

def Is_TamGiac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def ChuviTamGiac(a, b, c):
    if Is_TamGiac(a, b, c):
        return a + b + c
    else:
        raise ValueError("Ba cạnh không tạo thành một tam giác hợp lệ.")

def S_TamGiac(a, b, c):
    if Is_TamGiac(a, b, c):
        p = ChuviTamGiac(a, b, c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        raise ValueError("Ba cạnh không tạo thành một tam giác hợp lệ.")