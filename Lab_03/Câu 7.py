n= int( input(" Nhập n: "))
S= 0
if n<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
    for i in range( 1, n+ 1):
        S= S+ 1/ i
    print(" S= ", S)