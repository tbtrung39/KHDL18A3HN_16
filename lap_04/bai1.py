while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        break
    print("Vui lòng nhập lại số nguyên dương!")

#caua
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print("a.", S4)

#caub
S5 = 0
j = 1
count = 0
while count < n:
    S5 += j**3
    j += 2
    count += 1
print("b.", S5)

#cauc
S6 = 0
k = 2
while k <= 2*n:
    S6 += k**4
    k += 2
print("c.", S6)