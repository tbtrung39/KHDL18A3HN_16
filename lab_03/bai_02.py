n = int(input("nhập n:"))
print(f"các số hoàn hảo nhỏ hơn {n} là:", end =" ")
for i in range(1, n):
    tong_uoc = 0
    for a in range(1, i):
        if i % a == 0:
            tong_uoc += a
    if tong_uoc == i:
        print(i, end =" ")
print()

           