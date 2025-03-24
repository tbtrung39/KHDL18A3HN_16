chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
chuoi_tron = ""
vi_tri = 0
while vi_tri < len(chuoi_1) or vi_tri < len(chuoi_2):
    if vi_tri < len(chuoi_1):
        chuoi_tron += chuoi_1[vi_tri]
    if vi_tri < len(chuoi_2):
        chuoi_tron += chuoi_2[vi_tri]
    vi_tri += 1
print("Chuỗi trộn là:", chuoi_tron)