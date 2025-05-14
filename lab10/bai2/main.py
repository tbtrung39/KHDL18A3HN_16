import my_square

a, b = 5, 5
if my_square.is_Square(a, b):
    print("Là hình vuông.")
    print("Chu vi:", my_square.ChuViHinhVuong(a))
    print("Diện tích:", my_square.DienTichHinhVuong(a))
else:
    print("Không phải hình vuông.")
