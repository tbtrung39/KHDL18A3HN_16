A = set()

while True:
    n = int(input("Nhap so tu nhien (khong phsi so de thoat): "))
    if n != int():
        break
    A.add(n)

m = max(A)
n = min(A)
q = sum(A)

print('Phan tu nho nhat', n)
print('Phan tu lon nhat', m)
print('Tong phan tu', q)
