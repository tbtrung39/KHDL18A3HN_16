import math 
a = float(input("nhập vận vận tốc a của oto:"))
t = (a**4 * math.log(4)) / math.log(5)
print(f"thời gian ô tô chạy đến khi dừng lại là: {t:.2f} giây")
