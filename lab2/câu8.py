# Lương căn bản
luong_can_ban = 1350000

# Nhập thâm niên công tác
tnct = int(input("Nhập thâm niên công tác (tháng): "))

# Xác định hệ số theo thâm niên công tác
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

# Tính lương
luong = he_so * luong_can_ban

# In ra kết quả
print(f"Lương của nhân viên là: {luong:.0f} đồng")

