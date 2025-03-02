import math
# Nhập vận tốc ban đầu
a = int(input("Nhập vận tốc ban đầu của xe (a): "))
# Tính thời gian t để xe dừng
t = a / (4 * (math.log(5) / math.log(4)))
print("Thời gian để xe dừng lại là:", round(t, 2), "giây")