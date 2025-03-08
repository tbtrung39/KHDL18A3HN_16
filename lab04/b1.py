# câu a
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại n: "))
S4 = sum(i**2 for i in range(1, n+1))
print(f"Tổng S4: {S4}")

# câu b
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại n: "))
S5 = sum((2*i + 1)**3 for i in range(n))
print(f"Tổng S5: {S5}")

#câu c
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại n: "))
S6 = sum((2*i)**4 for i in range(1, n+1))
print(f"Tổng S6: {S6}")