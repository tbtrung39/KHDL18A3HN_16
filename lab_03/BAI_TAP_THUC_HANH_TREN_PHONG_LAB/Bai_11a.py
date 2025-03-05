n = int(input("Nhập số hàng (độ rộng ngang): "))

# Tam giác (a)
print("(a)")
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

