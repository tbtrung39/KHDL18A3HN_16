a = []
n = int(input("Nhap so luong phan tu: "))
print("Nhap cac phan tu:")
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)
dem = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            dem += 1
print("So cap chi so (i, j) thoa man la:", dem)