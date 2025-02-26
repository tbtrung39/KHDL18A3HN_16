#số nguyên có 3 chữ só
print("\n nhập số có 3 chữ số")
a=int(input("nhập chữ số hàng trăm"))
b=int(input("nhập vào chữ số hàng chục"))
c=int(input("nhập vào chữ số hàng đơn vị"))
if a<0:
    if b==0:
        print(f"âm {a} trăm lẻ {c}")
    elif b==1:
        print(f"âm {a} trăm mười {c} ")
    else:
        print(f"âm {a} trăm {b} mươi {c}")
elif a>0:
    if b==0:
        print(f" {a} trăm lẻ {c}")
    elif b==1:
        print(f" {a} trăm mười {c} ")
    else:
        print(f" {a} trăm {b} mươi {c}")
else:
    print("số không hợp lệ.Vui lòng nhập lại")
    