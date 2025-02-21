# Nhập giá trị x
x = float(input('Nhập giá trị x: '))

# Tính giá trị biểu thức f(x)
f = (-x + (x**2 + 4)**0.5) / ((x**4 + 1)**(1/7))

print('Giá trị của biểu thức là: %0.2f' % f)
