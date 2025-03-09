while True:
    n = int(input("Nhập n = "))
    cos = 0
    for i in range(1, n+1):
        cos += 1 - ((n**3)/(n * (n - 1)))
    print(round(cos, 4))
    break