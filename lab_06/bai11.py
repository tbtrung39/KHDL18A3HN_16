n=int(input("Nhap so phan tu cua danh sach A: "))
A=[int(input(f"nhap phan tu thu,{i+1}:")) for i in range(n)]
print("Danh sach a:",A)

B=[x for x in A if x%3==0 and x%5!=0]
print("Danh sach b:",B)

C=[x**2 for x in A]
print("Danh sach c:",C)

D=[A[i] for i in range(len(A)) if A[i]%3==0]
print("Danh sach d:",D)