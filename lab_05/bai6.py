s=input("nhap chuoi hex:")
hex_char="0123456789ABCDEFabcdef"
hex_str=""
for i in hex_char:
    hex_str +=i
if hex_str =="":
    print("khong co ki tu hop le trong he hex.")
else:
    print("chuoi he hex:",hex_str)
    print("gia tri thap phan:",int(hex_str,16))
    