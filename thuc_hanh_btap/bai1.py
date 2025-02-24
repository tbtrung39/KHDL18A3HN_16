print('\n\n\t\t=====THÁNG CÓ BAO NHIÊU NGÀY=====')
thang = int(input("Tháng cần tìm: "))
if thang == 1 or thang == 3 or thang == 5 or thang ==7 or thang == 8 or thang == 10 or thang == 12:
    print("Tháng có 31 ngày")
elif thang == 4 or thang == 6 or thang ==9 or thang == 11:
    print("Tháng có 30 ngày")
elif thang == 2:
    print("Tháng có 28 ngày vào năm không nhuận,29 ngày vào năm nhuận")
else:
    print("Chỉ có 12 tháng!!!")
