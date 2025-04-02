m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i+1} (các số cách nhau bởi dấu cách): ").split()))
    while len(hang) != n:  
        print(f" Hàng {i+1} phải có đúng {n} phần tử! Vui lòng nhập lại.")
        hang = list(map(int, input(f"Nhập hàng {i+1} lại: ").split()))
    A.append(hang)
print("\nMa trận A:")
for hang in A:
    print(hang)
tong = sum(sum(hang) for hang in A)
print("\nTổng các phần tử của ma trận là:", tong)
