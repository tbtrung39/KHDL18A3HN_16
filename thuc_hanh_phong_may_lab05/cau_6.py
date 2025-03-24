#Bài 6:
chuoi_nhap = input("Nhập chuỗi: ").upper()
danh_sach_hex = "0123456789ABCDEF"
chuoi_hop_le = ""
for ky_tu in chuoi_nhap:
    if ky_tu in danh_sach_hex:
        chuoi_hop_le += ky_tu
if chuoi_hop_le:
    gia_tri_thap_phan = int(chuoi_hop_le, 16)
    print("Chuỗi hợp lệ là:", chuoi_hop_le)
    print("Giá trị thập phân:", gia_tri_thap_phan)
else:
    print("Chuỗi không chứa ký tự hợp lệ trong hệ hex.")