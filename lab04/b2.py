while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        break
    print("Vui lòng nhập lại số nguyên dương!")

#caua
S_a = 0
sign = 1
for i in range(1, n + 1):
    S_a += sign * (1 / i)
    sign *= -1
print("a.", S_a)

#caub
S_b = 0
for i in range(2, n + 1):
    S_b += 1 / (i * (i - 1))
print("b.", S_b)

#cauc
import math
S_c = 0
i = 2
while i <= n:
    S_c += 1 / math.sqrt(i)
    i += 1
print("c.", S_c)
