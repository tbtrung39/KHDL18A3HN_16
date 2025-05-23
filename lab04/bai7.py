n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại n: "))
la_so_nguyen_to = [True] * n
la_so_nguyen_to[0] = la_so_nguyen_to[1] = False
for i in range(2, int(n**0.5) + 1):
    if la_so_nguyen_to[i]:
        for j in range(i*i, n, i):
            la_so_nguyen_to[j] = False
tong_cac_so_nguyen_to = sum(i for i in range(n) if la_so_nguyen_to[i])
print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {tong_cac_so_nguyen_to}")