n = int(input("nhập n: "))
t = 0
for i in range(1, n+1):
    if n % i == 0:
        t += 1
if t == 2:
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")
    so_nguyen_to_duoi = 0
    for duoi in range(n-1, 1, -1):
        t = 0
        for i in range(1, duoi + 1):
            if duoi % i == 0:
                t += 1
        if t == 2:
            so_nguyen_to_duoi = duoi 
            break
    so_nguyen_to_tren = 0
    for tren in range(n + 1, 1000000):
         t = 0
         for i in range(1, tren + 1):
             if tren % i == 0:
                  t += 1
         if t == 2:
             so_nguyen_to_tren = tren
             break
         if n - so_nguyen_to_duoi <= so_nguyen_to_tren - n:
             print(f"Số nguyên tố gần nhất là {so_nguyen_to_duoi}")
         else:
             print(f"Số nguyên tố gần nhất là {so_nguyen_to_tren}")
             
             
             
         