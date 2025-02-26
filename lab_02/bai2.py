import math 
a=float(input("nhập a:"))
b=float(input("nhập b:"))
c=float(input("nhập c:"))
print(f"{a}x**2 + {b}x +{c}")
if a==0:
    if b==0:
        if c==0: 
            print("phương trình vô số nghiệm")
        elif c!=0:
            print("phương trình vô nghiệm")
    elif b!=0:
        if c==0:
            print("phương trình có nghiệm =0 ")
        elif c!=0:
            print("phương trình có nghiệm duy nhất là:", -c/b)
elif a!=0:
    delta= b**2-4*a*c
    if delta >0:
        x1 = (b- math.sqrt(delta))/2*a
        x2 = (b + math.sqrt(delta))/2*a
        print(f"phương trình có 2 nghiệm phân biệt x1= {x1}, x2={x2}")
    elif delta==0:
        print("phương trình có nghiệm kép x= ", -b/2*a )
    elif delta <0:
        print("phương trình vô nghiệm")
  