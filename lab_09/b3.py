def sum_powers_of_2(n):
    if n == 1:
        return 2
    else:
        return 2**n + sum_powers_of_2(n-1)

n = int(input("Nhập số n: "))
result = sum_powers_of_2(n)
print("Tổng lũy thừa của 2 là:", result)
