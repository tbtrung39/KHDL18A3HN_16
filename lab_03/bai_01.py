n = int(input("nhập n:"))
tong = 1
tich = 1
for i in range(n):
    tich *= (2 * (i + 1)) / (2 * i + 3)
    tong += tich
print(f"tổng: {tong:.3f}")
