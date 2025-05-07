def ucln(tu_so, mau_so):
    return tu_so / mau_so

a = int(input("Nhap tu so: "))
while True:
    b = int(input("Nhap mau so: "))
    if b == 0:
        print("Nhap lai")
    else:
        ucln = ucln(tu_so = a, mau_so = b)
        print(f'Voi tu so: {a}, mau so: {b}, ta co UCLN la: {round(ucln, 2)}')
        break