#Bài 7:
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
ucln = a
b_temp = b
while b_temp != 0:
    ucln, b_temp = b_temp, ucln % b_temp
bcnn = abs(a * b) // ucln
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)
