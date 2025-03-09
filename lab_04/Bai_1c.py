while True:
    n = int(input("Nhập n = "))
    s6 = 0
    if n > 0:
        for i in range(1, n + 1):
            s6 += (2*i)**4
        print(f"2**4 + 4**4 + 6**4 + ... + (2*{n})**4 = {s6}")
        break
    else:
        print("n phải > 0.")