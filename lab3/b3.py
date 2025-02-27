n = int(input("Nhập số n: "))
nguyen_to = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        nguyen_to = False
        break

if nguyen_to and n > 1:
    print(f"{n} là số nguyên tố")
else:
    nguyen_to_duoi = n - 1
    for i in range(n-1, 1, -1):
        nguyen_to = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                nguyen_to = False
                break
        if nguyen_to:
            nguyen_to_duoi = i
            break
    nguyen_to_tren = n + 1
    tim_nguyen_to_tren = False
    for i in range(n + 1, 2 * n):
        nguyen_to = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                nguyen_to = False
                break
        if nguyen_to:
            nguyen_to_tren = i
            tim_nguyen_to_tren = True
            break
    if (n - nguyen_to_duoi) <= (nguyen_to_tren - n):
        print(f"{n} không phải là số nguyên tố. Số nguyên tố gần nhất là {nguyen_to_duoi}.")
    else:
        print(f"{n} không phải là số nguyên tố. Số nguyên tố gần nhất là {nguyen_to_tren}.")   
