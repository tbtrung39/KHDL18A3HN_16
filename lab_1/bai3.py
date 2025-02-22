r = float(input('Nhập số đo bán kính R: '))
h = float(input('Nhập số đo chiều cao: '))
sxq = 2*3.14*r*h
stp = 2*3.14*r*(h + r)
v = 3.14*r*r*h
print('Diện tích xung quanh của khối trụ là%0.2f'%sxq)
print('Diện tích toàn phần của khối trụ là%0.2f'%stp)
print('Thể tích của khối trụ là%0.2f'%v)
