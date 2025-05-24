thang = int(input("Nhập tháng:"))
if 1 <= thang <= 12:
    if thang == 1 or thang == 3 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print(f"Tháng {thang} có 31 ngày")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print(f"Tháng {thang} có 30 ngày")
    else:
        nam = int(input("Nhập năm:"))
        if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
            print(f"Tháng {thang} có 29 ngày")
        else:
            print(f"Tháng {thang} có 28 ngày")
else:
    print("Tháng không hợp lệ !")
    