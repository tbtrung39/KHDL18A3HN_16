tnct= int( input(" Nhập thâm niên công tác của nhân viên: "))
if tnct <= 0:
    print(" Không hợp lệ. Nhập lại.")
elif tnct< 12:
    he_so= 2.34
elif tnct>= 12 and tnct< 36:
    he_so= 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * 1350000
print(f"Lương của nhân viên: {luong} đồng")