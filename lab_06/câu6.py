import random

# Tạo list A gồm 1000 số ngẫu nhiên từ 1 đến 99999
A = [random.randint(1, 99999) for _ in range(1000)]

# In 10 phần tử đầu (chưa sắp xếp)
print("10 phần tử đầu (chưa sắp xếp):")
print(A[:10])

# --- Cách 1: Dùng hàm sorted() ---
A_sorted1 = sorted(A)  # Tạo bản sao đã sắp xếp

# --- Cách 2: Tự cài đặt thuật toán Selection Sort ---
n = len(A)
A_sorted2 = A.copy()
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if A_sorted2[j] < A_sorted2[min_idx]:
            min_idx = j
    A_sorted2[i], A_sorted2[min_idx] = A_sorted2[min_idx], A_sorted2[i]

# Kiểm tra kết quả
print("\n10 phần tử đầu (Cách 1 - sorted()):")
print(A_sorted1[:10])

print("\n10 phần tử đầu (Cách 2 - Selection Sort):")
print(A_sorted2[:10])

# Xác minh 2 cách giống nhau
if A_sorted1 == A_sorted2:
    print("\n✓ Hai phương pháp sắp xếp cho kết quả giống nhau.")
else:
    print("\n✗ Lỗi: Hai phương pháp sắp xếp cho kết quả khác nhau!")