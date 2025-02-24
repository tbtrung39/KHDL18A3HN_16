print('\n\n\t\t===== GIẢI PT BẬC 2 =====')

a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("PT vô số nghiệm.")
        else:
            print("PT vô nghiệm")
    else:
        print("PT bậc nhất có nghiệm: x =", -c / b)
else:
    delta = b * b - 4 * a * c
    print("Delta =", delta)  
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("PT có hai nghiệm phân biệt: x1 =", x1, ", x2 =", x2)
    elif delta == 0:
        x12 = -b / (2 * a)
        print("PT có nghiệm kép: x =", x12)
    else:
        print("PT vô nghiệm.")


