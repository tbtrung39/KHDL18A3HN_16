#Cách 1
chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")
gia_tri_thap_phan = int(chuoi_nhi_phan, 2)
print("Giá trị thập phân là:", gia_tri_thap_phan)

#Cách 2
chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")
gia_tri_thap_phan = 0
for vi_tri in range(len(chuoi_nhi_phan)):
    gia_tri_thap_phan = gia_tri_thap_phan * 2 + int(chuoi_nhi_phan[vi_tri])
print("Giá trị thập phân là:", gia_tri_thap_phan)