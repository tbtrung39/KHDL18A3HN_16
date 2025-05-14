
import my_square, my_Triange
a = float(input("nhap do dai canh hinh vuong:"))
chu_vi= my_square.ChuViHinhVuong(a)
dien_tich= my_square.DienTich_HinhVuong(a)
if a>0:
    print("chu vi hinh vuong",chu_vi)
    print("dien tich hinh vuong", dien_tich)
else:
    print("do dai canh hinh vuong khog hop le")
a = float(input("nhap canh a"))
b = float(input(" nhap canh b "))
c = float(input("nhap canh c"))
if my_Triange.is_TamGiac(a,b,c):
    print("day la tam giac")
    chu_vi = my_Triange.ChuviTamGiac(a,b,c)
    dien_tich= my_Triange.S_TamGiac(a,b,c)
    print("chu vi tam giac", chu_vi)
    print("dien tich tam giac", dien_tich)
else:
    print("3 canh khong tạo thanh 1 tam giac")
