a, b= input(" Nhập hai số nguyên dương: "). split()
a= int(a)
b= int(b)
a_goc= a
b_goc= b
# Tạo biến trung gian và gán cho b( WCLN( a, b) = WCLN( a, a% b= c) ) :
while b != 0:
    trunggian= b
    b= a% b
    a= trunggian
bcnn= int( (a_goc+ b_goc) / a)
print(" BCNN của {} và {} là ". format(a_goc,b_goc),bcnn)