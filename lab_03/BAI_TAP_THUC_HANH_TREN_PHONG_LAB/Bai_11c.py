n = int(input("Nhập số hàng (độ rộng ngang): "))
# Tam giác (c)
print("(c)")
for i in range(n):
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()