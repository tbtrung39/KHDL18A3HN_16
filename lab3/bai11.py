n = int(input("Nhap so hang cua tam giac: "))

# tam giac a
print("Tam giac sao dac:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#  tam giac b
print("\nTam giac sao rong:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

#tam giac c
print("\nTam giac sao rong kieu khac:")
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")