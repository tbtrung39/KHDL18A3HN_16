def tinh_luong(tnct):
    LUONG_CO_BAN = 135000
    if tnct < 12:
        he_so = 2.34
    elif 12 <= tnct < 36:
        he_so = 3.33
    elif 36 <= tnct < 60:
        he_so = 3.66
    else:
        he_so = 3.99
    luong = he_so * LUONG_CO_BAN
    return luong
# Nhập số tháng thâm niên công tác từ người dùng
try:
    tnct = int(input("Nhập số tháng thâm niên công tác: "))
    if tnct < 0:
        print("Thâm niên công tác không hợp lệ!")
    else:
        print(f"Lương của nhân viên: {tinh_luong(tnct):,.0f} đồng")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")