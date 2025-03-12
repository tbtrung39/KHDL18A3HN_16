n= int( input(" Nhập n: "))
gia_tri_tuyet_doi= abs(n)
tong= 0
while gia_tri_tuyet_doi> 0:
    tong= tong+ gia_tri_tuyet_doi % 10
    gia_tri_tuyet_doi= gia_tri_tuyet_doi // 10
print(" Tổng của những chữ số: ", tong)