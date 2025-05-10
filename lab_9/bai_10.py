def truy_hoi(n):
    x = 0
    if n == 0:
        x = 1
        return x
    else:
        for i in range(1, n + 1, -1):
            x += (n**2)*truy_hoi(n - 1)
        return x

n = int(input("Nhập n = "))
print(truy_hoi(n))