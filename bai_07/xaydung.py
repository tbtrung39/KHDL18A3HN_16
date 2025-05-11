import math

def day():
    A = [i for i in range(0, 101)]
    return A

def lietke():
    B = []
    for i in day():
        if i % 7 == 0:
            B.append(i)
    return B

def tong():
    return sum(lietke())

def kiemtra():
    C = []
    for i in day():
        for j in day():
            if math.sqrt(i) == j:
                C.append(i)
    return C