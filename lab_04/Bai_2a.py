while True:
    n = int(input("Nhập n = "))
    s = 1
    if n > 0:
        for i in range(1, n+1):
            s += (1/i)*(-1)**i
        print(s)
        break
    else:
        print("n phải > 0.")