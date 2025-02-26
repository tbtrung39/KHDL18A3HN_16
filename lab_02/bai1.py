n = int(input("nhập tháng"))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print(f"tháng {n} có 31 ngày")
elif n==2:
    print(f"tháng {n} có 28 hoặc 29 ngày")
elif n==4 or n==6 or n==9 or n==11:
    print(f"tháng {n} có 30 ngày")
else:
    print(f"tháng {n} không hợp lệ. Vui lòng nhập lại")










