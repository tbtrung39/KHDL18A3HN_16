def ucln(a, b):
    if a > b:
        return a/b
    elif a < b:
        return b/a

a = int(input("Nhap 1 so nguyên bất kỳ: "))
b = int(input("Nhap 1 so nguyên bất kỳ: "))
print(f'Uoc chung lon nhat cua {a}, {b} là: {ucln(a, b)}')