def ucln(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

n = int(input("Nhap n = "))

print('Uoc chung lon nhat cua', n, 'la:')
print(ucln(n))
