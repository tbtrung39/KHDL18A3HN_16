nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng (1-12): "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")
else:
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print(f"Tháng {thang} có 31 ngày.")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print(f"Tháng {thang} có 30 ngày.")
    else:  
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            print(f"Tháng 2 năm {thang} có 29 ngày (năm nhuận).")
        else:
            print(f"Tháng 2 năm {nam} có 28 ngày.")
