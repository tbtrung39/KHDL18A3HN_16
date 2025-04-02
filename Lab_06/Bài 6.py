import random
A = [random.randint(1, 99999) for i in range(1000)]
print (" List A gồm 1000 số ngẫu nhiêu là: ", A)
# Cách 1: Sử dụng sorted():
A_sorted = sorted(A)
print(" Sắp xếp danh sách theo thứ tự tăng dần: ", A_sorted)
# Cách 2: Sắp xếp trực tiếp bằng Bubble Sort:
A_copy = A[:]
n = len(A_copy)
for i in range(n - 1):
    for j in range(n - i - 1):
        if A_copy[j] > A_copy[j + 1]:
            A_copy[j], A_copy[j + 1] = A_copy[j + 1], A_copy[j]
print(" Sắp xếp danh sách theo thứ tự tăng dần: ", A_copy)