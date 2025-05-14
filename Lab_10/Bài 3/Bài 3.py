import sohoc
a, b= map( int, input(" Nhập hai số: ").split())
if a== b== 0:
    print(" Hai số không có UCLN. ")
else:
    if a!= 0 and b== 0:
        print(" UCLN: ", abs(a))
    else:
        if a== 0 and b!= 0:
            print(" UCLN: ", abs(b))
        else:
            ucln= sohoc.Ucln( a, b)
            bcnn= sohoc.Bcnn( a, b)
n= int( input(" Nhập n: "))
if n<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
    tong= sohoc.SumDivisor( n)