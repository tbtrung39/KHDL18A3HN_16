import sohoc

a, b = map(int,input("Nhap a, b: ").split(' '))
n = int(input("Nhap n = "))

if a != 0 or b != 0:
    print('ucln cua a va b la:', sohoc.ucln(a, b))
    print('bcnn cua a va b la:', sohoc.bcnn(a, b))

if n != 0:
    print('Tong cac uoc chung la:', sohoc.sumdivision(n))