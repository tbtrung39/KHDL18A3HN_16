# bài 1 
# nhập thông tin từ bàn phím 
thang = int(input("nhập tháng (1-12): "))
# kiểm tra số ngày của từng tháng 
if thang  ==1 or thang ==3 or thang ==5 or thang ==7 or thang ==8 or thang ==10 or thang ==12:
    print(f"tháng {thang} có 31 ngày")
elif thang ==4 or thang ==6 or thang ==11:
    print(f"thang {thang} có 30 ngày")
elif thang ==2:
    print("tháng 2 có 28 hoặc 29 ngày tùy vào năm nhuận")
else:
    print("tháng không hợp lệ! vui lòng nhập lại")