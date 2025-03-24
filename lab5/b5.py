chuoi_nhap = input("Nhập chuỗi ký tự: ")
chuoi_so = ''
for ky_tu in chuoi_nhap:
    if ky_tu.isdigit():
        chuoi_so += ky_tu
if chuoi_so == '':
    print("Không có số nào trong chuỗi.")
else:
    so_lay_duoc = int(chuoi_so)
    print("Số lấy được là:", so_lay_duoc)
    tong_uoc = 0
    for uoc in range(1, so_lay_duoc):
        if so_lay_duoc % uoc == 0:
            tong_uoc += uoc
    if tong_uoc == so_lay_duoc:
        print(so_lay_duoc, "là số hoàn hảo.")
    else:
        print(so_lay_duoc, "không phải là số hoàn hảo.")
#Bài 5 giống bài 7