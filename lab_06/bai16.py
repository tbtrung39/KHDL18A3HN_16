X=int(input("Nhap X: "))
Y=int(input("nhap Y: "))
ma_tran=[[i*j for j in range(Y)] for i in range(X)]
for hang in ma_tran:
    print(" ".join(f"{X:3}" for X in hang))