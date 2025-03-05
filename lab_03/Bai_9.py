n = int(input("Nhập n = "))
P = Q = R = 0
if n <= 0:
    print("Nhập lại")
else:
    for i in range(1, n + 1):
        P += i**2
        Q += (i + 1) * 3
        R += (2 * i)**4
    print(round(P), round(Q), round(R))