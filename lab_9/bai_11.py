def truy_hoi(n):
    m = 1
    p = 1
    q = 1
    if n == 0 or n == 1:
        m = 1
        return m
    elif n >= 2:
        m *= (n - 2)
        p *= m
        q = p * n
    return q

k = 999
S = 0
for i in range(1, k + 1):
    S += (-1)**(k + 1)*truy_hoi(k)
print(S)