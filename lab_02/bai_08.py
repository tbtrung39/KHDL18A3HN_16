thang_ct = int(input("nhập số tháng công tác:"))
luong_cb = 1350000
if thang_ct < 12:
    he_so = 2.34
elif 12 <= thang_ct < 36:
    he_so = 3.33
elif 36 <= thang_ct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong= he_so * luong_cb
print(f"lương nhân viên: {luong} đồng")


