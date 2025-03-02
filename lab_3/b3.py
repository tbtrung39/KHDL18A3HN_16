n = int(input("Nhập số n: "))
# kiểm tra số nguyên tố 
la_nguyen_to = True
if n < 2: 
    la_nguyen_to = False
for i in range(2, int(n**0.5)+1):
    if n % i ==0:
        la_nguyen_to = False
        break 
if la_nguyen_to:
    print(f"{n} là số nguyên tố")
else:
    # tìm số nguyên tố nhỏ hơn gần nhất 
    so_nho_nhat = -1 
    for x in range(n-1, 1, -1):
        la_nguyen_to = True
        for i in range(2, int(n**0.5)+1):
            if x % i ==0:
                la_nguyen_to = False
                break 
        if la_nguyen_to:
            so_nho_nhat = x
            break 
    # tìm số nguyên tố lớn hơn gần nhất 
    so_lon_nhat = -1 
    for x in range(n+1, n*2):
        la_nguyen_to = False
        for i in range(2, int(x**0.5)+1):
            if x % i ==0:
                la_nguyen_to = False
                break 
        if la_nguyen_to:
            so_lon_nhat = x
            break 
    # kiểm tra số nào gần n hơn 
    if so_nho_nhat != -1 and so_lon_nhat != -1:
        if (n - so_nho_nhat) <= (so_lon_nhat-n):
            print(f"số nguyên tố gần nhất: {so_nho_nhat}")
        else:
            print(f'số nguyên tố gần nhất: {so_lon_nhat}')
    elif so_nho_nhat != -1:
        print(f"số nguyên tố gần nhất: {so_nho_nhat}")
    else:
        print(f"số nguyên tố gần nhất: {so_lon_nhat}")