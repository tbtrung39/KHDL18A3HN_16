n = int(input("Nhập số nguyên dương: "))
print(f"Phân tích thừa số nguyên tố của {n}: ", end="")

for i in range(2, n + 1):
    if n % i == 0:
        print(i, end=" ")
        n //= i 