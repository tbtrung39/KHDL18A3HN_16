n = int(input("Nhập n = "))
D = {}

for i in range(1, n + 1):
    D.update({i: i*i})

print(D)