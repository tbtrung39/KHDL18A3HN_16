#1
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    n=int(input("Nhập lại n:"))
S4 = 0 
i = 1
while i<n:
    S4 += i**2
    i += 1
print(S4)
#2
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    n=int(input("Nhập lại n:"))
S5 = 0 
i = 1 
while i<=(2*n+1):
   S5+= i**3
   i+=2
print(S5)
#3
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    n=int(input("Nhập lại n:"))
S6 = 0
i += 2
while i<=2*n:
    S6 += i**4
    i += 2
print(S6)

    
