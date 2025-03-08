ky_tu = " "  
while ky_tu == " " or ky_tu == "":  
    ky_tu = input("Nhập một ký tự: ")  
    if ky_tu and ky_tu[1:]:  
        print("Vui lòng chỉ nhập một ký tự!")
        ky_tu = " "  
ASCCI_code = ord(ky_tu[0])
print("Mã ASCII của ký tự", ky_tu[0], "là:", ASCCI_code)