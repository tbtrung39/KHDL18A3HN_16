import random
A = set()
n = int(input("Nhập n từ bàn phím: "))
A = {random.uniform(0,100) for i in range(n)}
print("Tập hợp A sau khi random: ",A)
min_a = min(A)
max_a = min(A)
tong_pt = sum(A)
print("Phần tử nhỏ nhất: ",min_a)
print("Phần tử lớn nhất: ",max_a)
print("Tổng các phần tử: ",tong_pt)