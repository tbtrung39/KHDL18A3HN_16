n = int(input("Nhập số hàng của tam giác: "))

# tam giác a
print("Tam giác sao đặc:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#  tam giác b
print("\nTam giác sao rỗng:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

#tam giác c
print("\nTam giác sao rỗng kiểu khác:")
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")