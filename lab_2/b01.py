thang = int(input("nhập tháng (1-12)"))
if thang==1 or thang ==3 or thang ==5 or thang ==7 or thang==8 or thang== 10 or thang == 12 :
    print("tháng có 31 ngày")
elif thang ==4 or thang==6 or thang== 9 or thang==11:
    print("tháng có 30 ngày")
elif thang==2:
    print("tháng có 28 ngày")
else:
    print("tháng không tồn tại, vui lòng nhập lại")
    