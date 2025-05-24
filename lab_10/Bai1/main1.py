import my_Triange

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if my_Triange.Is_TamGiac(a, b, c):
    print("Là tam giác")
    print("Chu vi:", my_Triange.ChuviTamGiac(a, b, c))
    print("Diện tích:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Không phải tam giác")