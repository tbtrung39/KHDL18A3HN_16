m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        while True:
            element_str = input(f" Nhập phần tử A[ {i+1}][ {j+1}]: ")
            if element_str.isdigit():
                element = int(element_str)
                if element >= 0:
                    row.append(element)
                    break
                else:
                    print(" Vui lòng nhập số tự nhiên ( không âm). ")
            else:
                print(" Vui lòng nhập một số nguyên. ")
    A.append(row)
print(" Ma trận A vừa nhập: ", A)
tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]
print(" Tổng các phần tử của ma trận A: ", tong)