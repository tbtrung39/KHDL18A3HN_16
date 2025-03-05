n = int(input("Nhập n = "))
P = 1
for i in range(0, n + 1):
    P += 2/3
    for j in range(1, i):
        P *= (2*(n + 1))/(2*n + 3)

print(f'{round(P, 3)}')