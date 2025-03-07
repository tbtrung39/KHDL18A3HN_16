n = int(input("Nhập số n: "))
while n <= 1:
    n = int(input("Nhập lại số nguyên lớn hơn 1: "))
S, i = 0, 2
while i <= n:
    S += 1 / (i**0.5)
    i += 1
print("S =", S)
