n = int(input("Nhập số hàng của tam giác: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    # (a) Tam giác sao rỗng 
    print("\n(a) Tam giác sao rỗng :")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # (b) Tam giác sao rỗng 
    print("\n(b) Tam giác sao rỗng :")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j % 2 == 0 or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # (c) Tam giác sao rỗng 
    print("\n(c) Tam giác sao rỗng :")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
