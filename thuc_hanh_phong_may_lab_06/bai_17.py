#Bài 17:
n = int(input('Nhập n: '))
A = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    A.append(row)
for row in A:
    print(" ".join(f"{x:2}" for x in row))