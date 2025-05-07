import math
def elemental_number_smaller_than_n(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')

while True:
    n = int(input("Nhap 1 so nguyen bat ky: "))
    if n < 1:
        print("So nguyen to lon hon 2")
    else:
        print(f"So nguyen so nho hon {n} la:")
        elemental_number_smaller_than_n(n)
        break