#Bai 3:
ban_kinh = float(input("Nhập bán kính của khối trụ: "))
chieu_cao = float(input("Nhập chiều cao của khối trụ: "))
dien_tich_xung_quanh = 2 * 3.14 * ban_kinh * chieu_cao
dien_tich_toan_phan = 2 * 3.14 * ban_kinh * (ban_kinh + chieu_cao)
the_tich = 3.14 * ban_kinh ** 2 * chieu_cao

dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)

print("Diện tích xung quanh của khối trụ là:", dien_tich_xung_quanh)
print("Diện tích toàn phần của khối trụ là:", dien_tich_toan_phan)
print("Thể tích của khối trụ là:", the_tich)