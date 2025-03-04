#A
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Yêu cầu nhập lại số nguyên dương n:"))
S1 = 0
for i in range(1,n+1):
    S1 = (n*(n+1))/2
print(S1)
#B
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Yêu cầu nhập lại số nguyên dương n:"))
S2=0
for i in range(1,2*n+1,2):
    S2 += i
print("Tổng S2 =", S2)
print("Kết quả:",(n+1)**2)
#c 
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Yêu cầu nhập lại số nguyên dương n:"))
S3 = 0
for i in range(2,2*n,2):
    S3 += i
    ket_qua = n*(n+1)
print("Tổng S3:",S3)
print("Kết quả:",ket_qua)
