x=float(input('Nhap gia tri x (radian): '))
cos_x=1
term=1
n=0
while abs(term)>1e-4:
    n+=1
    term*=(-1)*x*x/((2*n)*(2*n-1))
    cos_x+=term
print(f"Gia tri gan dung cua cos({x}) la: {cos_x}")

        