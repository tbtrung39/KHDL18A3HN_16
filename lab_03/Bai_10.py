n = int(input("Nhập n = "))
for i in range(1, n + 1):
    if n % i == 0:
        n = n // i
        print(i, end=' ')