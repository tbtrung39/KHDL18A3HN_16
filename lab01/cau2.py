s = int(input("Nhập giây: "))
d = round(s / (24 * 3600), 2) 
h = round(s / 3600, 2)
m = round(s / 60, 2)
print("Số ngày là:", d)
print("Số giờ là:", h)
print("Số phút là:", m)
#
r = float(input("Nhập bán kính R: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14
Sxq = 2*pi*r*h
Stp = 2*pi*r*r + 2*pi*r*h
V = pi*r*r*h
print(f"Diện tích xung quanh: {Sxq:.2f}")
print(f"Diện tích toàn phần: {Stp:.2f}")
print(f"Thể tích khối trụ: {V:.2f}")
