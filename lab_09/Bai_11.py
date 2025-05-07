def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
def bcnn(a, b):
    return (a * b) // ucln(a, b)
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
if a <= 0 or b <= 0:
    print("Chi tinh BCNN cho hai so nguyen duong.")
else:
    ket_qua = bcnn(a, b)
    print(f"Boi chung nho nhat cua {a} va {b} la: {ket_qua}")