a=int(input('Nhap gia tri a = '))
b=int(input('Nhap gia tri b = '))
x,y=a,b
while y!=0:
    x,y=y,x%y
#tinh bcnn
bcnn=(a*b)//x
print(f"Boi chung nho nhat cua {a} va {b} la {bcnn}")