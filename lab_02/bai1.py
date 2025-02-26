a=int(input("nhap thang: "))
if a==2:
    print(f"thang {a} co 28 ngay")
elif a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print(f"thang {a} co 31 ngay")
elif a==4 or a==6 or a==9 or a==11:
    print(f"thang {a} co 30 ngay")
else:
    print("khong hop le vui long nhap lai")