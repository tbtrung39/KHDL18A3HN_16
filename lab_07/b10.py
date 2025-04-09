tong = 0
n = int(input("Nhap so luong so nguyen: "))
for i in range(n):
    so = input(f"Nhap so thu {i+1}: ")
    for chu in so:
        if chu.isdigit():
            tong += int(chu)
print("Tong cac chu so cua tat ca cac so la:", tong)
