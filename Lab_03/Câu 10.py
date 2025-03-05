n = int(input("Nhập n từ bàn phím: "))
n_goc = n
if n <= 0:
    print("Không hợp lệ. Nhập lại.")
else:
    print(f"Phân tích {n_goc} thành thừa số nguyên tố:", end=" ")
    first = True
    for i in range(2, n_goc + 1):
        dem = 0
        for j in range(n):
            if n % i == 0:
                dem= dem+ 1
                n= n/ i
            else:
                break
        if dem > 0:
            if not first:
                print(" x", end=" ")
            print(i, end="")
            if dem > 1:
                print(f"^{dem}", end="")
            first = False
        if n == 1:
            break
