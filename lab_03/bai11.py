#a
n = int(input("Nhập số hàng của tam giác: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "*")

#b
n = int(input("Nhập độ rộng của tam giác: "))

for i in range(n):
    for j in range(2 * n - 1):
        if j == n - 1 - i or j == n - 1 + i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#c
n = int(input("Nhập độ rộng của tam giác: "))

for i in range(n):
    for j in range(2 * n - 1):
        if j >= n - 1 - i and j <= n - 1 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
