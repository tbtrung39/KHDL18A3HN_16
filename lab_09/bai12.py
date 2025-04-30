def dem_chu_so(n):
    if n < 10:
        return 1
    else:
        return 1 + dem_chu_so(n // 10)
n = int(input("Nhap mot so nguyen duong: "))
if n <= 0:
    print("Chi dem chu so cua so nguyen duong.")
else:
    so_chu_so = dem_chu_so(n)
    print(f"So chu so cua {n} la: {so_chu_so}")