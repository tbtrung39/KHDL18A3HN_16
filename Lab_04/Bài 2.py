n= int( input(" Nhập n: "))
if n<= 0:
    print(" Không hợp lệ. Nhập lại. ")
else:
# Phần a:
    i= 1
    S1= 0
    while i<= n:
        if i % 2 == 0:
            S1 -= 1 / i
        else:
            S1 += 1 / i
        i= i+ 1
    print(" S1= ", S1)
# Phần b:
    j= 2
    S2= 0
    while j<= n:
        S2= S2+ 1/ j* ( j+ 1)
        j= j+ 1
    print(" S2= ", S2)
# Phần c:
    t= 2
    S3= 0
    while t<= n:
        S3= S3+ 1/ t** 1/ 2
        t= t+ 1
    print(" S3= ", S3)
