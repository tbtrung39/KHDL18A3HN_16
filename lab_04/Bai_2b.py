while True:
    n = int(input("Nhập n = "))
    s = 0
    if n > 0:
        for i in range(1, n+1):
            s += 1/(i * (i+1))
        print(s)
        break
    else:
        print("n phải > hơn 0.")