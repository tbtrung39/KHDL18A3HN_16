D = {}

for i in range(1, 101):
    D.update({i: str(bin(i)[2:])})

print(D)