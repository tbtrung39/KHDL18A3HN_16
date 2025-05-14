import my_square

a = int(input("Nhập cạnh a:"))
b = int(input("Nhập cạnh b:"))
if my_square.la_hinh_vuong(a, b):
    print("Là hình vuông.")
    print("Chu vi:", my_square.chu_vi_hinh_vuong(a))
    print("Diện tích:", my_square.dien_tich_hinh_vuong(a))
else:
    print("Không phải hình vuông.")
