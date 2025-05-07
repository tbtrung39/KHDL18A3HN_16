def so_sanh(a, b, c):
    if a > b > c:
        return a
    elif a < b > c:
        return b
    elif a < b < c:
        return c

a = int(input("Nhap 1 so nguyen bat ky: "))
b = int(input("Nhap 1 so nguyen bat ky: "))
c = int(input("Nhap 1 so nguyen bat ky: "))
print(f'So lon nhat trong 3 so {a}, {b}, {c} la: {so_sanh(a, b, c)}')