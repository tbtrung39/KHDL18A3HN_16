A = []
n = int(input("Nhap so luong phan tu cua tap hop A: "))
for i in range(n):
    x = input(f"Nhap phan tu thu {i+1}: ")
    A.append(x)
so_nguyen = 0
so_thuc = 0
chuoi = 0
for item in A:
    try:
        if '.' in item:
            float(item)  
            so_thuc += 1
        else:
            int(item)  
            so_nguyen += 1
    except:
        chuoi += 1
print("So luong so nguyen:", so_nguyen)
print("So luong so thuc:", so_thuc)
print("So luong chuoi ky tu:", chuoi)