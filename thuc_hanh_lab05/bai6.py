str = input("NHập chuỗi hex: ")
hex_char = "0123456789ABCDEFabcdef"
hex_str = ""
for i in str:
    if i in hex_char:
        hex_str += i
if hex_str == "":
    print("KHông có kí tự hợp lệ")
else:
    print("Chuỗi hệ hex: ",hex_str)
    print("Kết quả thập phân: ",int(hex_str,16))