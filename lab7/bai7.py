A=set()
B=set()
while True:
    n=input("Nhap ky tu tap hop A (nhan ESC de thoat): ")
    m=input("Nhap ky tu tap hop B (nhan ESC de thoat): ")
    if m=='ESC' and n=='ESC':
        break
    A.add(n)
    B.add(m)
print(A)
print(B)
print("Phan tu chung la:", A.intersection(B))