print("\n Nhập số có 3 chữ sốsố")
a=int(input('Nhập chữ số hàng tram: '))
b=int(input('Nhập chữ số hàng chục: '))
c=int(input('Nhập chữ số hàng đơn vị: '))
if a<0:
    if b==0:
        print(f"âm {a} trăm lẻ {c}")
    elif b==1:
        print(f"âm {a} trăm mười {c}")
    else:
        print(f"âm {a} trăm {b} mươi {c}")
elif a>0:
    if b==0:
        print(f" {a} trăm lẻ {c}")
    elif b==1:
        print(f" {a} trăm mười {c}")
    else:
        print(f" {a} trăm {b} mười {c}")
else:
    print("Không hợp lệ. Vui lòng nhập lại")