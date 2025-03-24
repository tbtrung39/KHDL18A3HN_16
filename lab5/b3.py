so_thap_phan = int(input("Nhập số nguyên dương: "))
chuoi_nhi_phan = ""
if so_thap_phan == 0:
    chuoi_nhi_phan = "0"
else:
    while so_thap_phan > 0:
        chuoi_nhi_phan = str(so_thap_phan % 2) + chuoi_nhi_phan
        so_thap_phan = so_thap_phan // 2
print("Chuỗi nhị phân là:", chuoi_nhi_phan)