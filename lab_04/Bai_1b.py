while True:
    n = int(input("Nhập n = "))
    s5 = 0
    if n > 0:
        for i in range(0, n + 1):
            s5 += (2*i + 1)**3
        print(f"1**3 + 3**3 + 5**3 + ... + (2*{n} + 1)**3 = {s5}")
        break
    else:
        print("n phải > hơn 0.")