n = int(input("Nhap n = "))
element_number = set()
for i in range(1, n + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            element_number.add(i)
print(element_number)