import math

def kiem_tra_tam_giac():
    try:
        a = float(input("Nhập độ dài cạnh a: "))
        b = float(input("Nhập độ dài cạnh b: "))
        c = float(input("Nhập độ dài cạnh c: "))

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Độ dài các cạnh phải là số dương.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba cạnh không thỏa mãn điều kiện tồn tại tam giác.")
        #Tính diện tích tam giác
        p = (a + b + c) / 2  
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Diện tích tam giác là: {S:.2f}")

    except ValueError as e:
        print("Lỗi:" ,e)

kiem_tra_tam_giac()