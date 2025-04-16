tu_dien = {}
for i in range(1, 101):
    tu_dien[i] = bin(i)[2:]
print("Tu dien gom cac cap (so: nhi phan):")
for k, v in tu_dien.items():
    print(f"{k}: {v}")