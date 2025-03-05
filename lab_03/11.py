n = int(input("Nhập số hàng: "))
for i in range(1):
    if n <= 0:
        print("Nhập lại, n phải là số nguyên dương!")
        n = int(input("Nhập số hàng: "))
#b
print("tam giác b:")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#c
print("tam giác c:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()