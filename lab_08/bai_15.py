lit = []

while True:
    n = input("Nhap 1 so nguyen bat ky: ")
    if n == 'q':
        break
    lit.append(n)

print(lit)
lit_bp = [int(i) for i in lit]
lit_bp = list(filter(lambda x: x % 2 != 0, lit_bp))
lit_bp = list(map(lambda x: x**2, lit_bp))
print(lit_bp)