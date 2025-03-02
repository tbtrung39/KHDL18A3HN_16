LUONG_CAN_BAN = 1350000  
tnct = int(input("Nhập số tháng thâm niên công tác: "))
if tnct >= 0:
    print("Thâm niên công tác không hợp lệ! Vui lòng nhập lại.")
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * LUONG_CAN_BAN
print(f"Hệ số lương: {he_so}")
print(f"Lương của nhân viên là: {luong:,.0f} đồng")
