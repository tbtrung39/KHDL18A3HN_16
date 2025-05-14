import my_square
a = float(input("Nhập cạnh hình vuông: "))
chu_vi=my_square.ChuViHinhVuong(a)
dien_tich=my_square.DienTich_HinhVuong(a)
if a >0:
    print("Chu vi hình vuông:",chu_vi)
    print("Diện tích hình vuông:",dien_tich)
