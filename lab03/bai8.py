n=int(input('Nhap mot so ngyuen duong n: '))
s1=0
s2=0
s3=0
if n<=0:
    print("Nhap sai vui long nhap lai")
else:
    for i in range(1,n+1):
        s1+=i
    for i in range(1,2*n+2,2):
        s2+=i
    for i in range(2,2*n+1,2):
        s3+=i
    print(f"s1 ={s1}")
    print(f"s2 ={s2}")
    print(f"s3 ={s3}")
