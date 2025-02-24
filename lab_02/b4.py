# Nhập vào một số nguyên
n = int(input("Nhập một số nguyên: "))

hang_tram = (n // 100) % 10

if n < 100:
    print(0)
else:
    print("Chữ số hàng trăm là:", hang_tram)
