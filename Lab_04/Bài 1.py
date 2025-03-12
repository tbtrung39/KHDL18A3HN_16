n= int( input(" Nhập n: "))
if n<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
# Phần a:
    i= 1
    S1= 0
    while i<= n:
        S1= S1+ i** 2
        i= i+ 1
    print(" S1= ", S1)
# Phần b:
    j= 1
    S2= 0
    while j<= n:
        S2= S2+ ( 2* j+ 1) ** 3
        j= j+ 1
    print(" S2= ", S2)
# Phần c:
    t= 2
    S3= 0
    while t<= n:
        S3= S3+ ( 2* j) ** 4
        t= t+ 1
    print(" S3= ", S3)
