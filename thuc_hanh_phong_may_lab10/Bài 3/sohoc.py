def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

def tong_uoc(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])
