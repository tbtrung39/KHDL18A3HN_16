
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b * b - 4 * a * c
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có một nghiệm: x =", round(x, 2))
else:
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép: x =", round(x, 2))
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", round(x1, 2))
        print("x2 =", round(x2, 2))
