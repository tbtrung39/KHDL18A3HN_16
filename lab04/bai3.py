
x = float(input("Nhập giá trị x (radian): "))
cos_x = 1  
term = 1  
n = 2  
sai_so = 10**-4
while True:
    term = (-term * x * x) / (n * (n - 1))  
    cos_x += term  
    if abs(term) < sai_so: 
        break
    n += 2  
print("Giá trị gần đúng của cos(x) là:", cos_x)
