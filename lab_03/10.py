n = int(input("Nhập số nguyên dương n: "))
x = 2
for i in range(1):
    if n <= 0:
        print("Nhập lại, n phải là số nguyên dương!")
        n = int(input("Nhập số nguyên dương n: "))
print("Các thừa số nguyên tố:")
for x in range(2, n+1):
    while n % x == 0:
        print(x)
        n = n // x
    if n == 1:
        break