n = int(input("Nhap n = "))
P = R = Q = 0
if n <= 0:
    print("Nhập lại")
else:
    for i in range(1, n):
        P += (i * (i + 1))/2
        R += (i + 1) * 2
        Q += i * (i + 1)
    print(round(P), round(R), round(Q))