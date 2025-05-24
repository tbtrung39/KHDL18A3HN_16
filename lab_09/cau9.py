def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Nhap so nguyen n: "))
ket_qua = fibonacci(n)
print(f"So Fibonacci thu {n} la: {ket_qua}")