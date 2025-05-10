def lon_nhat(a, b, c):
    if a > b > c:
        print(f"{a} lon nhat")
    elif a < b < c:
        print(f"{b} lon nhat")
    else:
        print(f"{c} lon nhat")

a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))
print(lon_nhat(a, b, c))
