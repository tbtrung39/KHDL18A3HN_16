# Cách 1: Dùng dictionary comprehension
tu_dien = {i: bin(i)[2:] for i in range(1, 101)}

for key, value in tu_dien.items():
    print(f"({key}, '{value}')")
# Cách 2: Dùng thuật toán thủ công để chuyển sang nhị phân
tu_dien = {}

for i in range(1, 101):
    n = i
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n //= 2
    tu_dien[i] = b

for key, value in tu_dien.items():
    print(f"({key}, '{value}')")
