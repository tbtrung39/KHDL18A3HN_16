import random
n = int(input("Nhập số lượng phần tử: "))
A = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    A.append(element)
# a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)
# b. Tạo danh sách C với các phần tử là bình phương của danh sách A
C = [x**2 for x in A]
print("Danh sách C:", C)
# c. Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3
D = [x for x in random.sample(A, random.randint(0, len(A))) if x % 3 == 0]
print("Danh sách D:", D)