Str = input("Nhập chuỗi: ")
he_hex = ""
check= True  
for i in Str:
    if not ( "A" <= i<= "F" or "0"<= i<= "9" ):
        check = False  
        break  
if check== True:
    print("Chuỗi nhập vào là hệ Hex.")
else:
    print("Chuỗi nhập vào không là hệ Hex.")
    chuoi_hex = ""
    for j in Str:
        if "A" <= j<= "F" or "0"<= j<= "9":
            chuoi_hex= chuoi_hex+ j
    if chuoi_hex == "":
        print(" Không thể chuyển đổi.")
    else:
        so_thap_phan = int(chuoi_hex, 16)
    print(" Chuỗi hex:", chuoi_hex)
    print("Giá trị thập phân:", so_thap_phan)