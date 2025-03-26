#câu 6: nhập một chuỗi Str từ bàn phím , kiểm tra chuỗi Str có phải là chuỗi.....
s = input("nhap chuoi hex: ")
hex_char = "0123456789ABCDEFabcdef"
hex_str = ""
for i in str:
    if i in hex_char:
        hex_str += i
if hex_str == "":
    print("khong co ky tu hop le trong phim hex.")
else:
    print("chuoi he hex", hex_str)
    print("gia tri nhap the:", int(hex_str,16))