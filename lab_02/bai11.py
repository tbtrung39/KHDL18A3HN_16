ngay=int(input("nhap ngay: "))
thang=int(input("nhap thang: "))
ngay_tiep_theo=ngay+1
if thang==2:
    if 0<ngay<28:   
        print(f"ngay tiep theo cua {ngay}/{thang} la {ngay_tiep_theo}/{thang}")
    elif ngay==28:
        print(f"ngay tiep theo cua {ngay}/{thang} la 1/{thang+1}")
    else:
        print("khong hop le vui long nhap lai")
elif thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10:
    if 0<ngay<31:   
        print(f"ngay tiep theo cua {ngay}/{thang} la {ngay_tiep_theo}/{thang}")
    elif ngay==31:
        print(f"ngay tiep theo cua {ngay}/{thang} la 1/{thang+1}")
    else:
        print("khong hop le vui long nhap lai")
elif thang==12:
    if 0<ngay<31:   
        print(f"ngay tiep theo cua {ngay}/{thang} la {ngay_tiep_theo}/{thang}")
    elif ngay==31:
        print(f"ngay tiep theo cua {ngay}/{thang} la 1/1")
    else:
        print("khong hop le vui long nhap lai")
elif thang==4 or thang==6 or thang==9 or thang==11:
    if 0<ngay<30:   
        print(f"ngay tiep theo cua {ngay}/{thang} la {ngay_tiep_theo}/{thang}")
    elif ngay==30:
        print(f"ngay tiep theo cua {ngay}/{thang} la 1/{thang+1}")
    else:
        print("khong hop le vui long nhap lai")
else:
    print("khong hop le vui long nhap lai")