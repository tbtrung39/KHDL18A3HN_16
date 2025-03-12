import math
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

a1, b1 = a, b
while b1:
    a1, b1 = b1, a1 % b1
ucln = a1

bcnn = abs(a * b) // ucln

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)