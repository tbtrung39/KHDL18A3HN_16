#Bài 2 :
def tim_ucln(so1, so2):
    if so2 == 0:
        return so1
    return tim_ucln(so2, so1 % so2)

def tim_ucln_danh_sach(danh_sach):
    if len(danh_sach) == 1:
        return danh_sach[0]
    return tim_ucln(danh_sach[0], tim_ucln_danh_sach(danh_sach[1:]))

so_luong = int(input("Nhập số lượng phần tử: "))
danh_sach_so = []
for _ in range(so_luong):
    danh_sach_so.append(int(input("Nhập số: ")))

ket_qua = tim_ucln_danh_sach(danh_sach_so)
print(f"Ước chung lớn nhất là: {ket_qua}")