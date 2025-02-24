a, b, c = map(float, input("nhập a,b,c: ").split())  
x = -b/(2*a)  
y = a*x**2+b*x+c  
print("đỉnh của pt bậc 2 là:", round(x, 2), round(y, 2))