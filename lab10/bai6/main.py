import doicoso2

s= input("NNhập chuỗi ký tự: ")
s= doicoso2.loc_ky_tu_hop_le(s)
print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", s)
print("Hệ cơ số của chuỗi là:", doicoso2.he_co_so(s))

print("Nhập chuỗi cơ số 2:")
print("=>", doicoso2.co_so2_sang_co_so10(input()))

print("Nhập chuỗi cơ số 8:")
print("=>", doicoso2.co_so8_sang_co_so10(input()))

print("Nhập chuỗi cơ số 16:")
print("=>", doicoso2.co_so16_sang_co_so10(input()))

