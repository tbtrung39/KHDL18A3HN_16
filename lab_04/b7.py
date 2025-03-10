# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

# Tìm ước chung lớn nhất (UCLN)
a1, b1 = a, b
while b1:
    a1, b1 = b1, a1 % b1
ucln = a1

# Tính bội chung nhỏ nhất (BCNN)
bcnn = abs(a * b) // ucln

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)
