str=input("Nhap chuoi: ")
he_hex=""
check=True
for i in str:
    if not ("A"<=i<="F" or "0"<=i<="9"):
        check=False
        break
if check==True:
    print("Chuoi nhap vao la he Hex")
else:
    print("Chuoi nhap vao khong la he Hex")
    chuoi_hex=""
    for j in str:
        if "A"<=j<="F" or "0"<=j<="9":
            chuoi_hex+=j
    if chuoi_hex=="":
        print("Khong the chuyen doi")
    else:
        so_thap_phan=int(chuoi_hex,16)
    print("Chuoi hex:",chuoi_hex)
    print("Gia tri thap phan:",so_thap_phan)