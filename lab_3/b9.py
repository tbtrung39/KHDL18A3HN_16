n = int(input("Nhập n (số nguyên dương): "))
if n <= 0:
    print("n phải là số nguyên dương.")
else:
    S4 = 0
    for i in range(1, n + 1):
        S4 += i**2
    print("S4 =", S4)
    S5 = 0
    for i in range(1, n + 1):
        S5 += (2*i - 1) ** 3
    print("S5 =", S5)
    S6 = 0
    for i in range(1, n + 1):
        S6 += (2*i) ** 4
    print("S6 =", S6)