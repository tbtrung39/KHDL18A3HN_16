import math
while True:
    n = int(input("Nhập n = "))
    s = 0
    if n > 0:
        for i in range(2, n+1):
            s += 1/math.sqrt(i)
        print(s)
        break
    else:
        print("n phải > hơn 0.")