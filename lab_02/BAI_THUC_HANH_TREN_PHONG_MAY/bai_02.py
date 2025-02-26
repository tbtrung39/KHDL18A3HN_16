a,b,c=map(float,input('Nhập độ dài các hệ số: ').split(","))
if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
           print('X bằng:',-c/b)

delta = b**2 - 4*a*c
import math
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('X1=',x1,'X2=',x2)
elif delta == 0:
    x = -b / (2*a)
    print('X=',x)
else:
    print('Phương trình vô nghiệm.')
