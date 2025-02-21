#câu 5

a = input("Nhập các phần tử của vector a, cách nhau bằng dấu cách: ").split()
a = [float(x) for x in a]


b = input("Nhập các phần tử của vector b, cách nhau bằng dấu cách: ").split()
b = [float(x) for x in b]


if len(a) != len(b):
    print("Hai vector phải có cùng số phần tử.")
else:
    
    tich_vo_huong = sum(x * y for x, y in zip(a, b))
    print("Tích vô hướng của hai vector a và b là:", tich_vo_huong)
