import my_Triange 
a = float(input("hay nhap canh  a: "))
b = float(input("hay nhap canh  b: "))
c = float(input("hay nhap canh c: "))
if my_Triange.is_TamGiac(a, b, c):
    print("day la mot tam giac.")
    print("Chu vi tam giac la:", my_Triange.ChuviTamGiac(a, b, c))

