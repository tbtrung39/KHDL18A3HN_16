#cach1
a = "01001100110"
chuoi_nhi_phan = ""
for ky_tu in a:
    if ky_tu in "01":  
        chuoi_nhi_phan += ky_tu
if chuoi_nhi_phan:
    so_thap_phan = int(chuoi_nhi_phan, 2)  
    print("Chuỗi nhị phân hợp lệ:", chuoi_nhi_phan)
    print("Giá trị thập phân:", so_thap_phan)
