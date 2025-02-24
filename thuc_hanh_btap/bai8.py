print('\n\n\t\t=====TÍNH LƯƠNG NHÂN VIÊN=====')
luong_can_ban = 1350000
# Nhập số tháng thâm niên công tác
tnct = int(input("Nhập số tháng thâm niên công tác: "))

# Xác định hệ số lương theo TNCT
if tnct < 12:
    he_so = 2.34
elif tnct < 36:
    he_so = 3.33
elif tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

# Tính lương
luong = he_so * luong_can_ban

# Xuất kết quả
print("Hệ số lương:", he_so)
print("Lương nhân viên:", int(luong), "VND")
