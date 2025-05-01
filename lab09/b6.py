import random

n = int(input("Nhập số n: "))
A = list(range(1, n + 1))
kqua = []

while A:
    # Chọn ngẫu nhiên một phần tử
    idx = random.randint(0, len(A) - 1)
    kqua.append(A[idx])
    A.pop(idx)  # Xóa phần tử đã chọn

print("Hoán vị ngẫu nhiên là:", kqua)
