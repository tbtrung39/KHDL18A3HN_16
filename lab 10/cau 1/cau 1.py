import my_Triange
a, b, c= map( float, input(" Nhập ba cạnh của tam giác: ").split())
if a<= 0 or b<= 0 or c<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
    check_tam_giac=my_Triange.is_TamGiac( a, b, c)
    chuvi= my_Triange.ChuviTamGiac( a, b, c)
    dientich= my_Triange.S_TamGiac( a, b, c)
    if check_tam_giac== True:
        print(" Ba cạnh tạo thành tam giác. ")
    else:
        print(" Ba cạnh không tạo thành tam giác. ")
    print(" Chu vi: ", chuvi)
    print(" Diện tích: ", dientich)