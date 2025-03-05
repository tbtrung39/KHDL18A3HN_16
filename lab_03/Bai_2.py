n = int(input("Nhập n = "))
P = 0
for i in range(1, n + 1):
    P += (2**(i - 1)) * ((2**i) - 1)
    print(P)