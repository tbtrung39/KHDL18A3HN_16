x= float( input(" Nhập vào số nguyên: "))
gia_tri_tuyet_doi= 0
if x>= 0:
    gia_tri_tuyet_doi= x
else:
    gia_tri_tuyet_doi= -x
hang_tram= gia_tri_tuyet_doi// 100
print(" Chữ số hàng trăm của số đó: ", hang_tram)