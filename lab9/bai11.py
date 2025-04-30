#a
def double_factorial(n):
    if n==0 or n==1:
        return 1
    return n * double_factorial(n-2)

#b
def calc_sum(k):
    S=0
    for i in range(1, k+1):
        S+=((-1)**i) * double_factorial(i)
    return S

k=int(input("Nhap k (k<1000): "))
print("Gia tri tong S la:", calc_sum(k))