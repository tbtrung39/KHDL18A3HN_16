n = int(input("nhaajpn(số nguyên dương): "))
while n <= 0:
    n = int(input("nhập lại n(phải lớn hơn 0): "))
# tính S4 
S4 = 0 
i = 1 
while i <= n: 
    S4 += i**2 
    i += 1 
print("S4 =", S4)
# tính S5 
S5 = 0 
i = 1 
while i <= n: 
    S5 = (2*1 - 1) **3 
    i += 1 
print("S5 =", S5)
# tính S6 
S6 = 0 
i = 1 
while i <= n: 
    S6 += (2**1)**4
print("S6 =", S6)