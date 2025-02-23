so = int(input("Nhập 1 số nguyên: "))
if so >= 100:
    hang_tram = so // 100 % 10
    print(f"Hàng trăm của {so} là {hang_tram}")
else:
    print("0")