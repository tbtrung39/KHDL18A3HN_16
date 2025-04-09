A = []

n = int(input("Input n = "))

for i in range(0, n + 1):
    A.insert(0, [])
    for j in range(0, i + 1):
        A[0].append(j)
    A[0].append(i)

print(A)