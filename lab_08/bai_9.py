def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return round(a / b, 2)

a = int(input("Nhập 1 số nguyên bất kỳ: "))
b = int(input("Nhập 1 số nguyên bất kỳ: "))
print(f'Phép tính cộng: {plus(a, b)}')
print(f'           trừ: {minus(a, b)}')
print(f'          nhân: {multiply(a, b)}')
print(f'          chia: {divide(a, b)}')