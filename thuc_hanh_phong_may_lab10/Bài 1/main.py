import my_Triangle

a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))

if a <= 0 or b <= 0 or c <= 0:
    print("Độ dài cạnh phải lớn hơn 0")
elif my_Triangle.la_tam_giac(a, b, c):
    print("Chu vi tam giác là:", my_Triangle.chu_vi_tam_giac(a, b, c))
    print("Diện tích tam giác:", round(my_Triangle.dien_tich_tam_giac(a, b, c), 2))