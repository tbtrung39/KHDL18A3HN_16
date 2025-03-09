while True:
    a = int(input("Nhập a = "))
    b = int(input("Nhập b = "))
    if b == 0 or a == 0:
        print("phải khác 0.")
    else:
        if a > b:
            print(f"BCNN của {a} và {b} là {a//b}")
            break
        else:
            print(f"BCNN của {a} và {b} là {b//a}")
            break