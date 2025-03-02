n = int(input("Nhập số n: "))  
if n < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(n,"là số nguyên tố.")
else:
    print(n,"không phải là số nguyên tố.")
    lower_prime = None
    for lower in range(n - 1, 1, -1):  
        is_lower_prime = True
        for i in range(2, int(lower ** 0.5) + 1):
            if lower % i == 0:
                is_lower_prime = False
                break
        if is_lower_prime:
            lower_prime = lower
            break  
    upper_prime = None
    for upper in range(n + 1, n + 1000):  
        is_upper_prime = True
        for i in range(2, int(upper ** 0.5) + 1):
            if upper % i == 0:
                is_upper_prime = False
                break
        if is_upper_prime:
            upper_prime = upper
            break  
    if lower_prime is not None and (upper_prime is None or (n - lower_prime) <= (upper_prime - n)):
        print(f"Số nguyên tố gần {n} nhất là {lower_prime}.")
    else:
        print(f"Số nguyên tố gần {n} nhất là {upper_prime}.")