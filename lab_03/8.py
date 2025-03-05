n = int(input("Nhập số nguyên dương n: "))
for i in range(1):
    if n <= 0:
        print("Nhập lại, n phải là số nguyên dương!")
        n = int(input("Nhập số nguyên dương n: "))
#a
S1 = n*(n+1)//2
print("S1 = ",S1)
#b
S2 = (n+1)**2
print("S2 =",S2)
#c
S3 = n*(n+1)
print("S3 =",S3)