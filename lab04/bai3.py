x=float(input("nhap gia tri x (radian): "))
# khoi tao gia tri ban dau
cos_x=1
term=1
n=0
# dung vong lap while de tinh cac gia tri gan dung cua cos(x)
while abs(term)>1e-4:
    n+=1
    term*=(-1)*x*x/((2*n)*(2*n-1))  # cong thuc truy hoi
    cos_x+=term
print(f"gia tri gan dung cua cos({x}) la: {cos_x}")

