import math


a = float(input('Nhập vận tốc ban đầu (a): '))

t = math.log(4) / (a**4 / 5)
t = round(t, 2)
print('Thời gian ô tô đi được cho đến lúc dừng là: %0.2f giây' % t)