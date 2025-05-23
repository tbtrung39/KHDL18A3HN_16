import math
def kiem_tra_tam_giac():
    try:
        a =  float(input("Nhập cạnh a: "))
        b =  float(input("Nhập cạnh b: "))
        c =  float(input("Nhập cạnh c: "))
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Các cạnh phải lớn hơn 0!!")
        if (a+b<=c) or (a+c<=b) or (b+c<=a):
            raise ValueError("3 cạnh không thoả mãn")
        cv = (a+b+c)/2
        S = math.sqrt(cv*(cv-a)*(cv-b)*(cv-c))
        print("S tam giác =: ",S)
    except ValueError as loi:
        if "KHông thể chuyển đổi" in str(loi):
            print("Lỗi, vui lòng nhập lại")
        else:
            print("Lỗi: ",loi)
kiem_tra_tam_giac()