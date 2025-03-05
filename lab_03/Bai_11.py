n = int(input("Nhập n = "))
#c
m = 2 * n - 2
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(end=' ')
    for j in range(1, i + 1):
        print('*', end=' ')
    m = m - 1
    print('\r')

#B
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=' ')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print('*', end=' ')
        else:
            print(" ", end=' ')
    print()

#A
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=' ')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print('*', end=' ')
        else:
            print(" ", end=' ')
    print()


