day=int(input("nhập ngày"))
month=int(input("nhập tháng"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
    if day>=1 and day<=30:
        print(f"ngày tiếp theo của {day}/{month} là {day+1}/{month}")
    elif day==31:
        print(f"ngày tiếp theo của {day}/{month} là 1/{month+1}")
    else:
        print("ngày tháng ko hợp lệ xin vui lòng nhập lại")
elif month==2:
    if day>=1 and day<=27:
        print(f"ngày tiếp theo của {day}/{month} là {day+1}/{month}")
    elif day==28:
        print(f"ngày tiếp theo của {day}/{month} là 1/{month+1}")
    else:
        print("ngày tháng không hợp lệ.Xin vui lòng nhập lại")
elif month==4 or month==6 or month==9 or month==11:
    if day>=1 and day<=29:
        print(f"ngày tiếp theo của {day}/{month} là {day+1}/{month}")
    elif day==30:
        print(f"ngày tiếp theo của {day}/{month} là 1/{month+1}")
    else:
        print("ngày tháng không hợp lệ.Xin vui lòng nhập lại")
elif month==12:
    if day>=1 and day<=30:
        print(f"ngày tiếp theo của {day}/{month} là {day+1}/{month}")
    elif day==31:
        print(f"ngày tiếp theo của {day}/{month} là 1/1 năm sau ")
    else:
        print("ngày tháng không hợp lệ.Xin vui lòng nhập lại")
else:
    print("tháng ko hợp lệ xin vui lòng nhập lại")