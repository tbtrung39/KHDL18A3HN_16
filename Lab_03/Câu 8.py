n= int(input(" Nhập số nguyên dương n: "))
S1= S2= S3= 0
if n<= 0:
    print(" Không hợp lệ. Nhập lại.")
else:
    for i in range( n+ 1):
        S1= S1+ i
        S2= S2+ ( 2* i+ 1)
        S3= S3+ 2* i
    print(" S1= ", S1)
    print(" S2= ", S2)
    print(" S3= ", S3)
