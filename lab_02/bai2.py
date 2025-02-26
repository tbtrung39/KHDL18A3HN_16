a,b,c=map(float,input("nhap he so a, b, c cua phuong trinh bac 2: ").split())
den_ta=b**2-4*a*c
if den_ta>0: 
    x1=(-b+(den_ta**(1/2)))/2*a
    x2=(-b-(den_ta**(1/2)))/2*a
    print(f"phuong co 2 nghiem phan biet la: x1={x1:.2f} va x2={x2:.2f}")
elif den_ta==0:
    x1=x2=-b/(2*a)
    print(f"phuong co 2 nghiem kep la: x1=x2={x1:.2f} ")
else:
    print("phuong tring vo nghiem")