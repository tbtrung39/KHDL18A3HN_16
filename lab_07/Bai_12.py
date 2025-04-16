n = int(input("Nhap so nguyen n: "))
tu_dien = {}
for i in range(1, n + 1):
    tu_dien[i] = i * i
print("Tu dien (i: i*i):")
print(tu_dien)