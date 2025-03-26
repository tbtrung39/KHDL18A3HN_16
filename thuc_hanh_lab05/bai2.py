str_nhap = input("Nhập chuỗi: ")
dem_ky_tu_khac = 0
for ky_tu in str_nhap:
    if not ky_tu.isalnum(): 
        dem_ky_tu_khac += 1
print("Số ký tự không phải chữ cái hoặc số:", dem_ky_tu_khac)

