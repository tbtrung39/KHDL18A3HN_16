def probability_at_least_one_six(n):
    p_no_six = (1 - 1/216) ** n  # Xác suất không có lần nào cả 3 xúc xắc ra 6
    p_at_least_one = 1 - p_no_six  # Xác suất ít nhất 1 lần cả 3 ra 6
    return round(p_at_least_one, 2)  # Làm tròn đến 2 chữ số thập phân
# Nhập số lần tung
n = int(input("Nhập số lần tung xúc xắc: "))
# Kiểm tra n hợp lệ
if n > 0:
    result = probability_at_least_one_six(n)
    print(f"Xác suất ít nhất 1 lần cả 3 xúc xắc ra 6 là: {result}")
else:
    print("Số lần tung phải lớn hơn 0!")