import math
a, b, c = map(float, input("Nhấp hệ số cho PTB2 ax^2 + bx + c = 0: "))
delta = (b**2) - (4 * a * c)
if delta < 0:
    print("PT vô nghiệm")
elif delta == 0:
    print(f"PT có nghiệm kép x1 = x2 = {-b/(2 * a)}")
elif delta > 0:
    x1 = (-b + math.sqrt(delta))/(2 * a)
    x2 = (-b - math.sqrt(delta))/(2 * a)
    print(f"PT có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
else:
    print("Nhập lại")