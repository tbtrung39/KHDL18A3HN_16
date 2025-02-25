ngay = int(input("nhập ngày:"))
thang =  int(input("nhập tháng:"))
nam = int(input("nhập năm:"))
if 1 <= thang <= 12:
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        ngay_trong_thang = 31
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        ngay_trong_thang = 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
            ngay_trong_thang = 29
        else:
           ngay_trong_thang = 28
    # kiểm tra ngày
    if 1 <= ngay <= ngay_trong_thang:
        if ngay < ngay_trong_thang:
            ngay += 1
        else:
            ngay = 1
            if thang < 12:
                thang += 1
            else:
                thang = 1
                nam += 1
        print(f"ngày tiếp theo là: {ngay}/{thang}/{nam}")
    else:
        print("ngày không hợp lệ vui lòng nhập lại")
else:
    print("tháng không hợp lệ! vui lòng nhập lại")
