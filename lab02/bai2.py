import math
a,b,c = map(float,input('Nhập các hệ số của phương trình bậcbậc 2: ').split())
print(f"{a}x**2 + {b}*x + {c}")
if a==0:
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệmnghiệm")
        elif c!=0:
            print("Phương trình vô nghiệmnghiệm")
    elif b!=0:
        if c==0:
            print("Phương trình có nghiệm = 0")
        elif c!=0:
            print("Phương trình có nghiệm duy nhất làlà:",-c/b)
elif a!=0:
    delta=b**2-4*a*c
    if delta>0:
        x1 = (b-math.sqrt(delta))/2*a
        x2 = (b+math.sqrt(delta))/2*a
        print("Phương trình có 2 nghiệm phân biệt làlà:",x1, x2)
    elif delta==0:
        print("Phương trình có nghiệm képkép x= ", -b/2*a)
    else:
        print("Phương trình vô nghiệmnghiệm")
