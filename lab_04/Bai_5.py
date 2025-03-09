while True:
    n = int(input("Nhập n = "))
    if n > 0:
        for i in range(n, -2, -1):
            print(i)
        break
    else:
        print("n lớn hơn 0")