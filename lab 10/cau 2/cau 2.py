import my_square as my_square
a= float( input(" Nhập cạnh của hình vuông: "))
if a<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
    chuvi= my_square.ChuviHinhVuong( a)
    dientich= my_square.Dien_tich_hinh_vuong( a)
    print(" Chu vi: ", chuvi)
    print(" Diện tích: ", dientich)