r, h = map(float, input("Nhập bán kính và chiều cao của khối trụ: "))
pi = 3.14
Sxq = 2 * pi * r * h
Stp = (2 * pi * r * h) + (2 * pi * (r**2))
V = pi * (r**2)
print(f"Diện tích xung quanh khối trụ là: {Sxq:.2f}")
print(f"Diện tích toàn phần khối trụ là: {Stp:.2f}")
print(f"Thể tích khối trụ là: {V:.2f}")