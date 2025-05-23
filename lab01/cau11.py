import math
a = float(input("Nhập vận tốc ban đầu: "))
if a <= 0:
    print("Vận tốc phải lớn hơn 0")
else:
    log10_4 = math.log10(4)
    log10_5 = math.log10(5)
    t = a * log10_4 / log10_5  
    print("Thời gian để xe dừng lại là:", round(t, 2), "giây")
