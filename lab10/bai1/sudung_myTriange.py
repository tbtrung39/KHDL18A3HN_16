import my_Triange

a, b, c = 3, 4, 5
if my_Triange.is_TamGiac(a, b, c):
    print("Là tam giác.")
    print("Chu vi:", my_Triange.ChuViTamGiac(a, b, c))
    print("Diện tích:", my_Triange.STamGiac(a, b, c))
else:
    print("Không phải tam giác.")