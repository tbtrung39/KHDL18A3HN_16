def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Nhập một số nguyên: "))
print(f"{number} là số nguyên tố!" if is_prime(number) else f"{number} không là số nguyên tố!")