import re  
mat_khau_nhap = input("Nhập danh sách mật khẩu, cách nhau bởi dấu phẩy: ")
mat_khau_danh_sach = mat_khau_nhap.split(",")
mat_khau_hop_le = []
for mat_khau in mat_khau_danh_sach:
    mat_khau = mat_khau.strip() 
    if not (6 <= len(mat_khau) <= 12):
        continue
    if (re.search("[a-z]", mat_khau) and  
        re.search("[A-Z]", mat_khau) and   
        re.search("[0-9]", mat_khau) and  
        re.search("[#@*]", mat_khau)):    
        
        mat_khau_hop_le.append(mat_khau)  
print("Mật khẩu hợp lệ:", ", ".join(mat_khau_hop_le) if mat_khau_hop_le else "Không có mật khẩu hợp lệ")
