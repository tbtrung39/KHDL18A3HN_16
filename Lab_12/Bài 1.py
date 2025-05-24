def kiem_tra_tam_giac( a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return " Lỗi: Cạnh tam giác phải > 0. "
    if a + b <= c or a + c <= b or b + c <= a:
        return " Lỗi: Ba cạnh không thỏa mãn điều kiện tạo thành tam giác. "
    return " Ba cạnh hợp lệ. Là tam giác. "
try:
    a = float(input(" Nhập cạnh a: "))
    b = float(input(" Nhập cạnh b: "))
    c = float(input(" Nhập cạnh c: "))
    print( kiem_tra_tam_giac( a, b, c))
except ValueError:
    print(" Lỗi: Dữ liệu nhập vào phải là số. ")