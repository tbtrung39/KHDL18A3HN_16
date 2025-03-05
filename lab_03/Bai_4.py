n = int(input("Nhập n = "))
P = 0
for i in range(2, n):
    for j in range(1, i):
        if j % 2 != 0 and j % 3 != 0 and j > 1 and j % i != 0 and j % i == 1:
            P = j
print(P)