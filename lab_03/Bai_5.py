row = int(input("Nhập hàng = "))
column = int(input("Nhập cột = "))
for i in range(row):
    print("*", end=" ")
    for j in range(column):
        print("*", end=" ")
    print("\r")
