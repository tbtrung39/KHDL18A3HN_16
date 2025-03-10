import math 
a = int(input("nhập số nguyên n: "))
b = int(input("nhập số nguyên b: " ))
# tính bcnn 
bcnn= abs(a*b)//math.gcd(a, b)
print(f"bội chung nhỏ nhất của {a} và {b} là: {bcnn}")