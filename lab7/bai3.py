A = set()

while True:
    n=int(input("Nhap so tu nhien: "))
    if n!=int():
        break
    A.add(n)

a=max(A)
b=min(A)
c=sum(A)

print("Phan tu lon nhat la:", a)
print("Phan tu nho nhat la:", b)
print("Tong phan tu:", c)