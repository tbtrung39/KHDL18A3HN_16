n = int(input("Nhập số phần tử Fibonacci (n): "))

# Tạo dãy Fibonacci bằng list comprehension
fibonacci = [0, 1]  # Khởi tạo 2 phần tử đầu
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n - 2)]

# In kết quả cách nhau bằng dấu ","
print("Dãy Fibonacci:", ", ".join(map(str, fibonacci[:n])))