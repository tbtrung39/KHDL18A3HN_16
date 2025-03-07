tu_so = float(input("Nhập tử số: "))
mau_so = 0
while mau_so == 0:
    mau_so = float(input("Nhập mẫu số: "))
    if mau_so == 0:
        print("Mẫu số không thể bằng 0. Vui lòng nhập lại.")
print("Phân số của bạn là:", tu_so, "/", mau_so)