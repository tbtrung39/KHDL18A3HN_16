n = int(input("Nhập n: "))
tong = 0.0
for i in range(1, n + 1):
    tong += 1 / i
print(f"Tổng  = {tong:.3f}")