#A
n = int(input("Nhập độ rộng của tam giác a:"))
print("\nTam giác (a):")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")  
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")  
        else:
            print(" ", end="")  
    print()
#B
n = int(input("Nhập số hàng của tam giác đều: "))
print("Tam giác đều b,")
for i in range(n):
    for j in range(2 * n - 1): 
        if j == n - i - 1 or j == n + i - 1:  
            print("*", end="")  
        elif i == n - 1 and (j % 2 == 0):  
            print("*", end="")
        else:
            print(" ", end="") 
    print()
#c
n = int(input("Nhập số hàng của tam giác: "))
print("Tam giác đặc c")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
