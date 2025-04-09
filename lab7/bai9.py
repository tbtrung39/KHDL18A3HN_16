n=int(input("Nhap n: "))
A=set()
B=set()
for i in range(0, 1001):
    if i>1:
        for j in range(2, i):
            if i%j==0:
                break
        else:
            if n%i==0:
                A.add(i)
            elif n%i!=0 and i<n:
                B.add(i)
print(A)
print(sorted(B))