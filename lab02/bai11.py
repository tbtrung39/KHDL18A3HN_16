a=int(input('Nhập ngày: '))
b=int(input('Nhập tháng: '))
if b==2:
    if 0<a<28:
        ngay_tiep_theo = a+1
        print(f"Ngày tiếp theo của {a}/{b} la {ngay_tiep_theo}/{b}")
    elif a==28:
        print(f"Ngày tiếp theo của {a}/{b} la 1/{b+1}")
    else: print("Không hợp lệ. Vui lòng nhập lại")
elif b==1 or b==3 or b==5 or b==7 or b==8 or b==10:
    if 0<a<31:
        ngay_tiep_theo=a+1
        print(f"Ngày tiếp theo của {a}/{b} laf {ngay_tiep_theo}/{b}")
    elif a==31:
        print(f"Ngày tiếp theo của {a}/{b} la 1/{b+1}")
    else: print("Không hợp lệ. Vui lòng nhập lại")
elif b==12:
    if 0<a<31:
        ngay_tiep_theo=a+1
        print(f"Ngày tiếp theo của {a}/{b} laf {ngay_tiep_theo}/{b}")
    elif a==31:
        print(f"Ngày tiếp theo của {a}/{b} la 1/1")
    else: print("Không hợp lệ. Vui lòng nhập lại")
elif b==4 or b==6 or b==9 or b==11:
    if 0<a<30:
        ngay_tiep_theo=a+1
        print(f"Ngày tiếp theo của {a}/{b} laf {ngay_tiep_theo}/{b}")
    elif a==30:
        print(f"Ngày tiếp theo của {a}/{b} la 1/{b+1}")
    else: print("Không hợp lệ. Vui lòng nhập lại")
else: 
    print("Không hợp lệ. Vui lòng nhập lại")
        