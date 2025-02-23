tnct = int(input("Nhập tháng: "))
luong_can_ban = 1350000
if tnct < 12:
    he_so = 2.34
    luong = he_so * luong_can_ban
    print(f"Lương của {tnct} tháng = {round(luong):_} đồng")
elif 12 <= tnct < 36:
    he_so = 3.33
    luong = he_so * luong_can_ban
    print(f"Lương của {tnct} tháng = {round(luong):_} đồng")
elif 36 <= tnct < 60:
    he_so = 3.66
    luong = he_so * luong_can_ban
    print(f"Lương của {tnct} tháng = {round(luong):_} đồng")
elif tnct >= 60:
    he_so = 3.99
    luong = he_so * luong_can_ban
    print(f"Lương của {tnct} tháng = {round(luong):_} đồng")
else:
    print("Nhập lại")