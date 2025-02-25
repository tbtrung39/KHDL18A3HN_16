thang = int(input("nhập tháng:"))
if 1 <= thang <= 12:
    if thang == 1:
        print("january")
    elif thang == 2:
        print("february")
    elif thang == 3:
        print("march")
    elif thang == 4:
        print("april")
    elif thang == 5:
        print("may")
    elif thang == 6:
        print("june")
    elif thang == 7:
        print("july")
    elif thang == 8:
        print("august")
    elif thang == 9:
        print("septempert")
    elif thang == 10:
        print("october")
    elif thang == 11:
        print("november")
    else:
        print("december")
else:
    print("tháng không hợp lệ ! vui lòng nhập lại")
    