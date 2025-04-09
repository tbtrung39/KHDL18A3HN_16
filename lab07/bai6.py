n = int(input("Nhập số tự nhiên n từ bàn phím: "))
list = []
a = 2
while len(list) < n:
    kt_so_nguyen_to = True
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            kt_so_nguyen_to = False
            break
    if kt_so_nguyen_to:
        list.append(a)
    a += 1
print("Dãy", n, "số nguyên tố đầu tiên:", list)