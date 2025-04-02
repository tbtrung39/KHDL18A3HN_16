m=int(input("Nhap so hang m: "))
n=int(input("Nhap so cot n: "))
A=[]
for i in range(m):
    hang=list(map(int,input(f"Nhap hang {i+1}: ").split()))
    if len(hang)!=m:
        print(f"Hang {i+1} phai co dung {n} phan tu")
        break
    A.append(hang)

tong=0
for i in range(m):
    for j in range(n):
        tong+=A[i][j]

print("Ma tran A:")
for hang in A:
    print(" ".join(map(str,hang)))
print("Tong cac phan tu cua ma tran A:",tong)