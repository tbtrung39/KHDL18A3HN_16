import random

# Nhập danh sách A từ bàn phím (ví dụ: 3, 15, 9, 20)
A = list(map(int, input("Nhập các số nguyên cách nhau bằng dấu phẩy: ").split(',')))

# a. Danh sách B: chia hết cho 3, không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B (chia hết 3, không chia hết 5):", B)

# b. Danh sách C: bình phương của A
C = [x**2 for x in A]
print("Danh sách C (bình phương của A):", C)

# c. Danh sách D: phần tử ngẫu nhiên từ A chia hết cho 3
D = random.choice([x for x in A if x % 3 == 0]) if any(x % 3 == 0 for x in A) else "Không có số chia hết cho 3"
print("Phần tử ngẫu nhiên từ A chia hết cho 3:", D)