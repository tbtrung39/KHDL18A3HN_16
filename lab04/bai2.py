n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n: "))
# a
S1 = 0
i = 1
while i <= n:
    if i % 2 == 1:  
        S1 += 1 / i
    else:  
        S1 -= 1 / i
    i += 1
print( S1)
#b
S2 = 0
i = 2
while i <= n:
    S2 += 1 / (i * (i + 1))
    i += 1
print(S2)
#c
S3 = 0
i = 2
while i <= n:
    S3 += 1 / (i ** 0.5)  
    i += 1
print(S3)
