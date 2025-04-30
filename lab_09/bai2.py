def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
def ucln_day(so_list, n):
    if n == 1:
        return so_list[0]
    return ucln(so_list[n-1], ucln_day(so_list, n-1))
n = int(input("Nhap so luong phan tu: "))
so_list = []
for i in range(n):
    so = int(input(f"Nhap so thu {i+1}: "))
    so_list.append(so)
ket_qua = ucln_day(so_list, n)
print("Uoc chung lon nhat la:", ket_qua)