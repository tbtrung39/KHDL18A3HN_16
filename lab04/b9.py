n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print(f"Giai thừa của {n} là: {giai_thua}")