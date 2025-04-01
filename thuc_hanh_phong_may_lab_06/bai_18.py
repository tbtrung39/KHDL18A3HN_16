#Bài 18:
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    if len(hang) != n:
        print(f"Hàng {i+1} phải có đúng {n} phần tử!")
        break
    A.append(hang)

tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]

print("Ma trận A:")
for hang in A:
    print(" ".join(map(str, hang)))
print("Tổng các phần tử của ma trận A:", tong)