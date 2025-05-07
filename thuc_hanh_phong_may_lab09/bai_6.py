#Bài 6:
import random

so_n = int(input("Nhập số n: "))
mang = list(range(1, so_n + 1))
ket_qua = []

while mang:
    chi_so = random.randint(0, len(mang) - 1)
    ket_qua.append(mang[chi_so])
    mang.pop(chi_so)

print(f"Hoán vị ngẫu nhiên: {ket_qua}")