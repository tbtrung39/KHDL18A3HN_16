n = int(input("nhập n:"))
t = 0
for a in range(2,n + 1):
    s = 0 
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            s += 1
            if i != a // i:
                s += 1
        if s > 2:
            break 
    if s == 2:
        print(a, end="")