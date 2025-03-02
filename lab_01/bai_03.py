# Nhập bán kính và chiều cao từ bàn phím
ban_kinh = float(input("Nhập bán kính r: "))
chieu_cao = float(input("Nhập chiều cao h: "))
pi = 3.14
dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao
dien_tich_toan_phan = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)
the_tich = pi * (ban_kinh ** 2) * chieu_cao
print("\n===== Kết Quả =====")
print("Diện tích xung quanh:", round(dien_tich_xung_quanh, 2))
print("Diện tích toàn phần:", round(dien_tich_toan_phan, 2))
print("Thể tích khối trụ:", round(the_tich, 2))