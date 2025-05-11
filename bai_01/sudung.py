import my_Triangle
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))

if my_Triangle.is_tamgiac(a, b, c):
    print("Chu vi tam giac la: ", my_Triangle.chuvitamgaic(a, b, c))
    print("Dien tich tam giac", my_Triangle.s_tamgiac(a, b, c))
