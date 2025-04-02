n = int(input("Nhập số phần tử Fibonacci (n): "))

# Khởi tạo danh sách Fibonacci
fibonacci = [0, 1]
for _ in range(n - 2):
    so_moi = fibonacci[-1] + fibonacci[-2]  # Tính số tiếp theo
    fibonacci.append(so_moi)  # Thêm vào danh sách

# In kết quả với dấu phẩy phân tách
print("Dãy Fibonacci:", ", ".join(map(str, fibonacci[:n])))