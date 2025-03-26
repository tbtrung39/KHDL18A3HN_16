n = int(input("Nhập số tự nhiên: "))
if n<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
    chuoi_nhi_phan = "" 
    if n == 0:
        chuoi_nhi_phan = "0" 
        print("Chuỗi nhị phân:", chuoi_nhi_phan)
    else:
        while n > 0:
            phan_du = n % 2  
            chuoi_nhi_phan = str(phan_du) + chuoi_nhi_phan
            n = n // 2  
        print("Chuỗi nhị phân:", chuoi_nhi_phan)