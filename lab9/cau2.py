def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

def ucln_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return ucln(numbers[0], ucln_list(numbers[1:]))

# Nhập n số
n = int(input("Nhập số lượng phần tử: "))
numbers = []
for _ in range(n):
    numbers.append(int(input("Nhập số: ")))

# Tính UCLN
result = ucln_list(numbers)
print("Ước chung lớn nhất là:", result)