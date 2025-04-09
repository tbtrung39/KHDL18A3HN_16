n = int(input("Nhập n = "))
number = set()

for i in range(2, n + 1):  
    a = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            a = False
            break
    if a:
        number.add(i)

print("Tập hợp các số nguyên tố từ 1 đến", n, "là:",number)
