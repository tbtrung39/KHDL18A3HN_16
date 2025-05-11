def ucln(a, b):
    if a % b == 0:
        return f'{round(a/b)}'
    else:
        return f'{round(b/a)}'

def bcnn(a, b):
    return f'{a * b}'

def sumdivision(n):
    A = []
    for i in range(1, n):
        if n % i == 0:
            A.append(i)
    return sum(A)