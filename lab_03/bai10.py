n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương: "))

print("Phân tích thừa số nguyên tố của", n, "là:", end=" ")

i = 2
while n > 1:
    while n % i == 0:
        print(i, end=" ")
        n //= i
    i += 1
