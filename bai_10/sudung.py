from hinhhoc import my_square as hinh_vuong
from hinhhoc import my_Triangle as tam_giac

n = int(input("Nhap canh hinh vuong: "))
a, b, c = map(int, input("Nhap canh tam giac: ").split(' '))

while tam_giac.is_tamgiac(a, b, c):
    print('Chu vi tam giac:', tam_giac.chuvitamgaic(a, b, c))
    print('Dien tich tam giac:', tam_giac.s_tamgiac(a, b, c))
    break

print('Chu vi hinh vuong la:', hinh_vuong.chuvihinhvuong(n))
print('Dien tich hinh vuonh la:', hinh_vuong.dien_tich_hinh_vuong(n))
