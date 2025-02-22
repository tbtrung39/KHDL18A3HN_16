a = float(input('Nhập giá trị a: '))
b = float(input('Nhập giá trị b: '))
c = float(input('Nhập giá trị c: '))
x = -b/2*a
delta = b*b - 4*a*c
y = -delta/4*a
print(f'Đỉnh của phương trình bậc 2: ({x:.2f}, {y:.2f})')
