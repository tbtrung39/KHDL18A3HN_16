def X(n):
    if n==0:
        return 1
    total=0
    for i in range(n):
        total+=(n-1)**2*X(i)
    return total

n=int(input("Nhap n: "))
print(f"Gia tri X_{n} la:", X(n))