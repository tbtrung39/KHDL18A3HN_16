#câu 3
# Nhập bán kính và chiều cao từ bàn phím
ban_kinh = float(input("Nhập bán kính: "))
chieu_cao = float(input("Nhập chiều cao: "))
pi = 3.14
dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao
dien_tich_toan_phan = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)
the_tich = pi * ban_kinh**2 * chieu_cao
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)
print("Diện tích xung quanh:", dien_tich_xung_quanh)
print("Diện tích toàn phần:", dien_tich_toan_phan)
print("Thể tích:", the_tich)