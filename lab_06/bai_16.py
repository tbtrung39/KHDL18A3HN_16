X = int(input("input X = "))
Y = int(input("Input Y = "))

a = []

for i in range(0, X):
    a.insert(0, [])
    for j in range(0, Y):
        a[i][0].append(1)

print(a)