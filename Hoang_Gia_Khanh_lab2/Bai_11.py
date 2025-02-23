ngay, thang = map(int,input("Nhập ngày và tháng: ").split(' '))
thang_1 = thang_3 = thang_5 = thang_7 = thang_8 = thang_10 = thang_12 = 31
thang_2 = 28
thang_4 = thang_6 = thang_9 = thang_11 = 30
if thang == 1:
    if ngay == thang_1:
        ngay = 1
        thang = 2
    else:
        ngay += 1
elif thang == 2:
    if ngay == thang_2:
        ngay = 1
        thang = 3
    else:
        ngay += 1
elif thang == 3:
    if ngay == thang_3:
        ngay = 1
        thang = 4
    else:
        ngay += 1
elif thang == 4:
    if ngay == thang_4:
        ngay = 1
        thang = 5
    else:
        ngay += 1
elif thang == 5:
    if ngay == thang_5:
        ngay = 1
        thang = 6
    else:
        ngay += 1
elif thang == 6:
    if ngay == thang_6:
        ngay = 1
        thang = 7
    else:
        ngay += 1
elif thang == 7:
    if ngay == thang_7:
        ngay = 1
        thang = 8
    else:
        ngay += 1
elif thang == 8:
    if ngay == thang_8:
        ngay = 1
        thang = 9
    else:
        ngay += 1
elif thang == 9:
    if ngay == thang_9:
        ngay = 1
        thang = 10
    else:
        ngay += 1
elif thang == 10:
    if ngay == thang_10:
        ngay = 1
        thang = 11
    else:
        ngay += 1
elif thang == 11:
    if ngay == thang_11:
        ngay = 1
        thang = 12
    else:
        ngay += 1
elif thang == 12:
    if ngay == thang_12:
        ngay = 1
        thang = 1
    else:
        ngay += 1
print(f"Ngày tiếp theo là: {ngay}/{thang}")