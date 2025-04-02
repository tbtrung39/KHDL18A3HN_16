import random

# Tạo list A gồm 1000 số ngẫu nhiên từ 1 đến 99999
A = [random.randint(1, 99999) for _ in range(1000)]

# In 10 phần tử đầu (chưa sắp xếp)
print("10 phần tử đầu (chưa sắp xếp):")
print(A[:10])

# --- Cách 1: Dùng hàm sorted() ---
A_sorted1 = sorted(A)  # Tạo bản sao đã sắp xếp

# --- Cách 2: Tự cài đặt thuật toán (Selection Sort - Đơn giản và dễ kiểm tra) ---
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

A_sorted2 = selection_sort(A.copy())  # Sắp xếp trên bản sao

# Kiểm tra kết quả
print("\n10 phần tử đầu (Cách 1 - sorted()):")
print(A_sorted1[:10])

print("\n10 phần tử đầu (Cách 2 - Selection Sort):")
print(A_sorted2[:10])

# Xác minh 2 cách giống nhau
print("\nHai kết quả khớp nhau?", A_sorted1 == A_sorted2)

# Kiểm tra tính đúng đắn bằng assert
assert A_sorted1 == A_sorted2, "Lỗi: Hai cách sắp xếp cho kết quả khác nhau!"
print("✓ Đã xác minh: Cả hai cách đều chính xác.")