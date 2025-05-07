def tim_max(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        return tim_max(b, c, a)
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
print("Số lớn nhất là:", tim_max(a, b, c))
