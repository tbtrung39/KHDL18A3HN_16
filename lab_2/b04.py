import math

# Nhập số nguyên từ người dùng
n = int(input("Nhập một số nguyên: "))

# Lấy chữ số hàng trăm
hang_tram = abs(n) // 100 % 10

# Xuất kết quả
print(f"Chữ số hàng trăm là: {hang_tram}")
