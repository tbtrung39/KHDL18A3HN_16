while True:
    n = int(input("Nhập n = "))
    s4 = 0
    if n > 0:
        for i in range(0, n + 1):
            s4 += i**2
        print(f'1**2 + 2**2 + 3**2 + ... + {n}**2 = {s4}')
        break
    else:
        print("n phải > hơn 0.")