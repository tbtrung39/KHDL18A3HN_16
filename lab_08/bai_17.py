from functools import reduce

n = int(input("Nhap 1 so nguyen bat ky: "))
lt = [i for i in range(1, n + 1)]
lit = list(filter(lambda x: x%2==0, lt))
ltit = reduce(lambda x, y: x + y, lit)
print(ltit)