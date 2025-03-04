#a
print("\n\n\t====Câu 9A=====\n\n\t")
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Yêu cầu nhập lại số nguyên dương n:"))
S4 = 0
for i in range(1,n+1):
    S4 += i**2
print("Kết quả S4:",S4)
#b
print("\n\n\t====Câu 9B=====\n\n\t")
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Yêu cầu nhập lại số nguyên dương n:"))
S5 = 0
for i in range(1,2*n+1,2):
    S5 += i**3
print("Kết quả:",S5)
#c
print("\n\n\t====Câu 9C=====\n\n\t")
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Yêu cầu nhập lại số nguyên dương n:"))
S6 = 0  
for i in range(2,2*n,2):
    S6 += i**4
print("Kết quả:",S6)