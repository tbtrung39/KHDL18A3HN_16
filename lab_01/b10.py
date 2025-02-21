import math

x = float(input('Nhập giá trị x: '))

f = math.log(x, 4) + math.log(2, x)

f = round(f, 2)

print('Giá trị của biểu thức là: %0.2f' % f)
