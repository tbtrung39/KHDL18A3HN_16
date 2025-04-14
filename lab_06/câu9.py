# Nhập list từ bàn phím (ví dụ: 2, 4, 6, 8)
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu phẩy: ").split(',')))

# Kiểm tra tất cả là số chẵn
assert all(num % 2 == 0 for num in numbers), "Lỗi: Có số không chẵn trong list!"

print("Tất cả số trong list đều chẵn:", numbers)
# Nhập list từ bàn phím (ví dụ: 2, 4, 6, 8)
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu phẩy: ").split(',')))

# Kiểm tra tất cả là số chẵn
assert all(num % 2 == 0 for num in numbers), "Lỗi: Có số không chẵn trong list!"

print("Tất cả số trong list đều chẵn:", numbers)