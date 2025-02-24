n = int(input("Nhập một số nguyên: "))
if n < 100:
    print(0)
elif n >= 100:
    print((n // 100) % 10)

