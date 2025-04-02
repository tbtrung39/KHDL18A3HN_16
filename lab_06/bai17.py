n=int(input("nhap bac cua ma tran don vi: "))
a=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
print("ma tran don vi bac ",n,"la: ")
for row in a:
    print(" ".join(map(str,row)))