A = set()
B = set()
while True:
    m = input("Nhap ky tu tap hop A (nhan ESC de thoat): ")
    n = input("Nhap ky tu tap hop B (nhan CSE de thoat): ")
    if m == 'ESC' and n == 'CSE':
        break
    A.add(m)
    B.add(n)
print(A)
print(B)

print('Phần tử chung:', A.intersection(B))
