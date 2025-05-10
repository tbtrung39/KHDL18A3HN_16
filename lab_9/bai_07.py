def bo_nghiem(n):
    if n == 1:
        return 1
    else:
        return bo_nghiem(n - 1)

n = int(input("Nhap n = "))
print(bo_nghiem(n))