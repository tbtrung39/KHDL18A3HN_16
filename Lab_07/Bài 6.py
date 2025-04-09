n = int(input("Nhập số tự nhiên n: "))
count = 0
number = 2
print("Dãy", n, "số nguyên tố đầu tiên: ")
while count < n:
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        print( number, end=' ')
        count += 1
    number += 1
