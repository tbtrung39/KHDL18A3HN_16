n= int(input("nhap so n:"))
print("cac so nguyen to nho hon hoac bang {n} la:",end=" ")
for num in range(2,n+1):
    is_prime=True
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")
