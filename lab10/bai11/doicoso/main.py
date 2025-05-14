import doicoso1, doicoso2

print("Chuyển từ thập phân sang hệ khác")
n = int(input("Nhập số nguyên hệ 10: "))
print("Nhị phân:", doicoso1.thap_phan_sang_nhi_phan(n))
print("Bát phân:", doicoso1.thap_phan_sang_bat_phan(n))
print("Thập lục phân:", doicoso1.thap_phan_sang_thap_luc(n))

print("Chuyển từ hệ khác sang hệ thập phân")
s = input("Nhập chuỗi số (có thể là hệ 2, 8 hoặc 16): ")

if doicoso2.la_he_2(s):
    print("Hệ 2 → Thập phân:", doicoso2.co_so2_sang_co_so10(s))
elif doicoso2.la_he_8(s):
    print("Hệ 8 → Thập phân:", doicoso2.co_so8_sang_co_so10(s))
elif doicoso2.la_he_16(s):
    print("Hệ 16 → Thập phân:", doicoso2.co_so16_sang_co_so10(s))
else:
    print("Không xác định được hệ của chuỗi số!")
