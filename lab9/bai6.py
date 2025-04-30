import random

n = int(input("Nhap so n: "))
A = list(range(1, n+1))
result = []

while A:
    idx = random.randint(0, len(A)-1)
    result.append(A[idx])
    A.pop(idx)  # Xoá phan tu đã chọn

print("Hoan vi ngau nhien:", result)