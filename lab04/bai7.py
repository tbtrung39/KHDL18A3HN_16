a=int(input("nhap gia tri m = "))
b=int(input("nhap gia tri n = "))
x,y=a,b
while y!=0:
    x,y=y,x%y

# tinh BCNN
bcnn=(a*b)//x
print(f"boi chung nho nhat cua {a} va {b} la {bcnn}")