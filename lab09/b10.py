def X(n):
    return 1  # Giả sử X(n) luôn trả về 1, bạn có thể thay đổi logic tùy ý

def tinh_tong(n):
    total = 0
    for i in range(n):
        total += (n - i ** 2) * X(n)  # Chỉnh sửa công thức
    return total

n = int(input("Nhập số n: "))
print("Giá trị tổng là:", tinh_tong(n))
