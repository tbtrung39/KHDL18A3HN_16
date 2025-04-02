number = int(input("Nhập một số nguyên: "))

is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

print(f"{number} là số nguyên tố!" if is_prime else f"{number} không là số nguyên tố!")

