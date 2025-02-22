import math
LUONG_CAN_BAN = 1350000
tnct = int(input("Nhập số tháng thâm niên công tác: "))

if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

luong = he_so * LUONG_CAN_BAN
print(f"Lương của nhân viên: {luong} đồng")
