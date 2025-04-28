import random

n = int(input("Nhập số n: "))
A = list(range(1, n+1))
result = []

while A:
    # Chọn ngẫu nhiên 1 phần tử
    idx = random.randint(0, len(A)-1)
    result.append(A[idx])
    A.pop(idx)  # Xoá phần tử đã chọn

print("Hoán vị ngẫu nhiên:", result)
