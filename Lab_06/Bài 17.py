n = int(input("Nhập kích thước ma trận đơn vị: "))
ma_tran = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    ma_tran.append(hang)
print("Ma trận đơn vị bậc", n, ":")
for hang in ma_tran:
    print(hang)