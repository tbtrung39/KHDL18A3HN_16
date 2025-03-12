import math

x = float(input("Nhập giá trị x (radians): "))

cos_x = 1
term = 1  
k = 1
fact = 1  

while abs(term) > 1e-4:
    fact *= (2 * k - 1) * (2 * k)  
    term *= - (x ** 2) / fact  
    cos_x += term  
    k += 1

print("Giá trị xấp xỉ của cos(x) là:", cos_x)