def nam_nhuan(y):
    if y % 4 == 0:
        print("Nam nhuan")
    else:
        print("Nam thuan")

while True:
    y = int(input("Nhap nam: "))
    if len(str(y)) != 4:
        print("Nhap lai.")
    else:
        nam_nhuan(y)
        break

def thang(m):
    if y % 4 == 0:
        if m in [1, 3, 5, 7, 8, 10, 12]:
            print("31 days")
        elif m in [4, 6, 9, 11]:
            print("30 days")
        elif m == 2:
            print("29 days")
    else:
        if m in [1, 3, 5, 7, 8, 10, 12]:
            print("31 days")
        elif m in [4, 6, 9, 11]:
            print("30 days")
        elif m == 2:
            print("28 days")

while True:
    m = int(input("Nhap thang: "))
    if m not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        print("Nhap lai")
    else:
        thang(m)
        break