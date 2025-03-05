n = int(input("Nhập số nguyên dương n: "))
for i in range(1):
    if n <= 0:
        print("Nhập lại, n phải là số nguyên dương")
        n = int(input("Nhập số nguyên dương n: "))
#a
S4 = 0
for i in range(1, n+1):
    S4 = S4 + i**2
print("S4 =",S4)
#b
S5 = 0
for i in range(n+1):
    S5 = S5 + (2*i+1)**3
print("S5 =",S5)
#c
S6 = 0
for i in range(1, n+1):
    S6 = S6 + (2*i)**4
print("S6 =",S6)