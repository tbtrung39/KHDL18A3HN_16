import my_square, my_Triangle

print("Tam Giác")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if my_Triangle.la_tam_giac(a, b, c):
    print("Đây là tam giác hợp lệ.")
    print("Chu vi tam giác:", my_Triangle.chu_vi_tam_giac(a, b, c))
    print("Diện tích tam giác:", round(my_Triangle.dien_tich_tam_giac(a, b, c), 2))
else:
    print("Ba cạnh không tạo thành tam giác.")


print("Hình Vuông")
canh1 = float(input("Nhập cạnh thứ nhất: "))
canh2 = float(input("Nhập cạnh thứ hai: "))

if my_square.la_hinh_vuong(canh1, canh2):
    print("Đây là hình vuông.")
    print("Chu vi hình vuông:", my_square.chu_vi_hinh_vuong(canh1))
    print("Diện tích hình vuông:", my_square.dien_tich_hinh_vuong(canh1))
else:
    print("Hai cạnh không bằng nhau nên không phải hình vuông.")